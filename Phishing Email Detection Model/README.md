# Phishing Email Detection Model

A Scikit-learn machine learning project that classifies email text as **Phishing** or **Safe**.

## Features

- TF-IDF text feature extraction
- URL count and URL-related features
- Suspicious keyword features
- Logistic Regression classifier
- Train/test split
- Accuracy calculation
- Classification report
- Confusion matrix
- Saved model with Joblib
- Command-line prediction of a new email

## Project structure

```text
phishing_email_detection_model/
├── data/
│   └── emails.csv
├── models/
├── main.py
├── predict.py
├── requirements.txt
└── README.md
```

## 1. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

## 2. Install dependencies

```powershell
pip install -r requirements.txt
```

## 3. Train the model

```powershell
python main.py
```

The program will:
1. Read `data/emails.csv`.
2. Split the data into training and testing sets.
3. Convert email text into TF-IDF features.
4. Extract URL/keyword features.
5. Train Logistic Regression.
6. Print accuracy and a classification report.
7. Generate `confusion_matrix.png`.
8. Save the trained model in `models/`.

## 4. Test a new email

After training:

```powershell
python predict.py
```

Example:

```text
Paste the email text:
> URGENT! Your account is suspended. Verify your password at http://example.com

Prediction : Phishing
Confidence : ...
```

## Dataset format

Replace `data/emails.csv` with a larger real-world dataset when submitting the final project.

Required columns:

```csv
email_text,label
"Your email content here","Safe"
"Urgent verify your account at http://...","Phishing"
```

Labels must be `Phishing` or `Safe`.

### Recommended final dataset

For a stronger internship submission, use a publicly available phishing/legitimate email dataset with hundreds or thousands of examples. Do not claim that the small included demo dataset represents real-world accuracy.

## How the model works

### 1. TF-IDF

TF-IDF converts words and word combinations into numerical values. Words that are useful for distinguishing messages receive stronger weights.

### 2. URL features

The model also counts:
- Number of URLs
- Message length
- Exclamation marks
- Dollar signs
- Suspicious keywords
- Urgency language
- Requests for passwords/card information

### 3. Classification

Logistic Regression learns the relationship between these features and the `Phishing`/`Safe` labels.

### 4. Evaluation

The project reports:
- Accuracy
- Precision
- Recall
- F1-score
- Confusion matrix

For phishing detection, **recall for the Phishing class is especially important**, because missing a phishing email can be more serious than incorrectly flagging a safe email.

## Important limitation

The included CSV is a small demonstration dataset so the project runs immediately. Its accuracy should **not** be presented as production performance. For your final internship report, train and test on a substantially larger, representative dataset and report the resulting metrics.

## Security note

This project is for defensive email-security learning. A prediction is not proof that an email is safe or malicious.
