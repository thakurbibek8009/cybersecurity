# 🔐 Password Strength Analyzer (Python)

A command-line based **Password Strength Analyzer** built using Python that evaluates the strength of a password and provides suggestions to improve security.

---

## 🚀 Features

* ✅ Checks password strength (Weak / Medium / Strong)
* ✅ Validates:

  * Password length
  * Uppercase letters
  * Lowercase letters
  * Numbers
  * Special characters
* ✅ Provides improvement suggestions
* ✅ Generates a stronger password suggestion
* ✅ Beginner-friendly and easy to understand

---

## 🛠️ Technologies Used

* **Python 3**
* **Regex (re module)**

---

## 📂 Project Structure

```id="1p7y7l"
Password-Strength-Analyzer/
│── password_analyzer.py
│── README.md
```

---

## ▶️ How to Run

1. Make sure Python is installed

   ```bash
   python --version
   ```

2. Clone the repository

   ```bash
   git clone https://github.com/your-username/password-strength-analyzer.git
   ```

3. Navigate to the project folder

   ```bash
   cd password-strength-analyzer
   ```

4. Run the script

   ```bash
   python password_analyzer.py
   ```

---

## 🧪 Example Usage

```id="3yq6yd"
Enter your password: abc123

Strength: Weak

Suggestions to improve:
- Add at least one uppercase letter
- Add at least one special character
- Password should be at least 8 characters long

Suggested Strong Password:
abc123A@XXXX
```

---

## 🧠 How It Works

The program analyzes the password based on:

* Length (minimum 8–12 characters)
* Presence of uppercase letters
* Presence of lowercase letters
* Presence of digits
* Presence of special characters

Each condition increases the score, and based on the score, the password is classified as:

* 🔴 Weak
* 🟡 Medium
* 🟢 Strong

---

## 🔒 Learning Outcomes

This project helps you understand:

* Basics of **Cybersecurity & Password Security**
* **Regular Expressions (Regex)** in Python
* Input validation techniques
* Writing clean and structured Python programs

---

## 💡 Future Enhancements

* 🔐 Store passwords securely using hashing (bcrypt)
* 🗄️ Prevent reuse of old passwords using a database
* 🖥️ Add GUI using Tkinter
* 🌐 Convert into a web application

---

## 🙌 Acknowledgement

This project was developed as part of a **Cybersecurity Virtual Internship** to learn password security and validation techniques.

---

## 📬 Contact

* GitHub: https://github.com/thakurbibek8009
* LinkedIn: https://linkedin.com/in/bibek-thakkur 
---

⭐ If you like this project, consider giving it a star!
