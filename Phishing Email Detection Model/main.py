import re
from pathlib import Path

import joblib
import matplotlib.pyplot as plt
import pandas as pd
from scipy.sparse import hstack, csr_matrix
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score, classification_report, confusion_matrix,
    ConfusionMatrixDisplay
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import FeatureUnion

DATA_PATH = Path("data/emails.csv")
MODEL_DIR = Path("models")
MODEL_DIR.mkdir(exist_ok=True)

URL_RE = re.compile(r"https?://\S+|www\.\S+", re.I)
KEYWORDS = [
    "urgent", "verify", "verification", "password", "account", "suspended",
    "click", "claim", "prize", "winner", "bank", "payment", "invoice",
    "security", "confirm", "login", "reward", "gift", "expire"
]

def url_features(text):
    text = str(text)
    urls = URL_RE.findall(text)
    lower = text.lower()
    return [
        len(urls),
        len(text),
        text.count("!"),
        text.count("$"),
        sum(lower.count(k) for k in KEYWORDS),
        int(any(k in lower for k in ["urgent", "immediately", "within 24 hours"])),
        int("password" in lower or "card information" in lower),
    ]

def build_features(train_texts, test_texts):
    tfidf = TfidfVectorizer(
        lowercase=True,
        stop_words="english",
        ngram_range=(1, 2),
        min_df=1,
        max_df=0.98,
        sublinear_tf=True
    )
    X_train_text = tfidf.fit_transform(train_texts)
    X_test_text = tfidf.transform(test_texts)

    X_train_url = csr_matrix([url_features(x) for x in train_texts])
    X_test_url = csr_matrix([url_features(x) for x in test_texts])

    return hstack([X_train_text, X_train_url]), hstack([X_test_text, X_test_url]), tfidf

def main():
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Dataset not found: {DATA_PATH}")

    df = pd.read_csv(DATA_PATH).dropna(subset=["email_text", "label"])
    df["label"] = df["label"].str.strip().str.title()

    X_train_text, X_test_text, y_train, y_test = train_test_split(
        df["email_text"],
        df["label"],
        test_size=0.25,
        random_state=42,
        stratify=df["label"]
    )

    X_train, X_test, tfidf = build_features(X_train_text, X_test_text)

    model = LogisticRegression(max_iter=2000, class_weight="balanced")
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    print("\n=== PHISHING EMAIL DETECTION MODEL ===")
    print(f"Dataset size : {len(df)} emails")
    print(f"Test size    : {len(y_test)} emails")
    print(f"Accuracy     : {accuracy:.2%}\n")
    print(classification_report(y_test, predictions, zero_division=0))

    labels = ["Phishing", "Safe"]
    cm = confusion_matrix(y_test, predictions, labels=labels)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)
    disp.plot(values_format="d")
    plt.title("Phishing Email Detection - Confusion Matrix")
    plt.tight_layout()
    plt.savefig("confusion_matrix.png", dpi=150)
    plt.show()

    joblib.dump(tfidf, MODEL_DIR / "tfidf_vectorizer.joblib")
    joblib.dump(model, MODEL_DIR / "phishing_model.joblib")
    print("Saved model to models/phishing_model.joblib")
    print("Saved vectorizer to models/tfidf_vectorizer.joblib")

def predict_email(email):
    tfidf = joblib.load(MODEL_DIR / "tfidf_vectorizer.joblib")
    model = joblib.load(MODEL_DIR / "phishing_model.joblib")
    text_matrix = tfidf.transform([email])
    url_matrix = csr_matrix([url_features(email)])
    features = hstack([text_matrix, url_matrix])
    label = model.predict(features)[0]
    confidence = max(model.predict_proba(features)[0])
    return label, confidence

if __name__ == "__main__":
    main()
