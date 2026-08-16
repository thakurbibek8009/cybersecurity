from main import predict_email

print("=== EMAIL PHISHING CHECKER ===")
email = input("\nPaste the email text:\n> ").strip()

if not email:
    print("Please enter an email.")
else:
    label, confidence = predict_email(email)
    print(f"\nPrediction : {label}")
    print(f"Confidence : {confidence:.2%}")
