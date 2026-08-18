# 🔐 Secure Login System

A secure user authentication web application built using **Python, Flask, SQLite, and bcrypt**.

The project demonstrates how to build a basic login system with secure password storage, input validation, SQL injection protection, session management, and logout functionality.

---

## 🎯 Project Objective

The main objective of this project is to create a secure login system that protects user accounts from common authentication attacks.

The application allows users to:

* Create an account
* Login securely
* Access a protected dashboard
* Logout from their account
* Store passwords securely using bcrypt

---

## ✨ Key Features

* 👤 User registration
* 🔑 Secure login
* 🔐 Bcrypt password hashing
* 🛡️ SQL injection protection
* ✅ Server-side input validation
* 🍪 Session management
* 🚪 Secure logout
* 🔒 Protected dashboard
* 📱 Responsive user interface
* 💾 SQLite database

---

## 🛠️ Technologies Used

| Technology | Purpose                   |
| ---------- | ------------------------- |
| Python     | Main programming language |
| Flask      | Web framework             |
| SQLite     | Database                  |
| bcrypt     | Password hashing          |
| HTML5      | Web page structure        |
| CSS3       | User interface styling    |

---

# 📂 Project Structure

```text
Secure_Login_System/
│
├── app.py
├── requirements.txt
├── README.md
│
├── templates/
│   ├── login.html
│   ├── register.html
│   └── dashboard.html
│
├── static/
│   └── style.css
│
└── instance/
    └── users.db
```

---

# 🔄 How the System Works

The application follows this authentication flow:

```text
             User
              │
              ▼
       Registration
              │
              ▼
      Validate Input
              │
              ▼
      Hash Password
         using bcrypt
              │
              ▼
      Store User in DB
              │
              ▼
            Login
              │
              ▼
       Check Password
              │
        ┌─────┴─────┐
        ▼           ▼
     Correct     Incorrect
        │           │
        ▼           ▼
 Create Session    Reject
        │
        ▼
    Dashboard
        │
        ▼
      Logout
        │
        ▼
 Clear Session
```

---

# 🔐 Security Features

## 1. Password Hashing

Passwords are **never stored as plain text**.

During registration, the password is converted into a secure bcrypt hash:

```python
password_hash = bcrypt.hashpw(
    password.encode("utf-8"),
    bcrypt.gensalt()
)
```

The database stores the resulting hash instead of the original password.

Example:

```text
User enters:
MyPassword123

Database stores:
$2b$12$...
```

This means someone who views the database cannot directly see the user's password.

---

# 2. Password Verification

During login, the entered password is compared with the stored bcrypt hash:

```python
bcrypt.checkpw(...)
```

If the password matches:

```text
Login successful
      ↓
Create session
      ↓
Open dashboard
```

If it does not match:

```text
Login rejected
```

---

# 3. SQL Injection Protection

The application uses **parameterized SQL queries**.

Example:

```python
db.execute(
    "SELECT * FROM users WHERE email = ?",
    (email,)
)
```

User input is not directly inserted into the SQL statement.

This helps prevent attacks such as:

```text
' OR '1'='1
```

---

# 4. Input Validation

The registration system validates user input.

### Username

```text
Minimum: 3 characters
Maximum: 30 characters
```

### Email

The application checks that an email address is provided in a valid basic format.

### Password

```text
Minimum: 8 characters
Maximum: 72 characters
```

Validation is performed on the **server**, so it cannot be bypassed simply by modifying the browser's HTML.

---

# 5. Session Management

After successful login, Flask creates a session:

```python
session["user_id"] = user["id"]
session["username"] = user["username"]
```

The session tells the application that the user is authenticated.

---

# 6. Protected Dashboard

The dashboard cannot be accessed directly without logging in.

The project uses a `login_required` decorator:

```python
@login_required
def dashboard():
    ...
```

If a user tries to access:

```text
/dashboard
```

without logging in, they are redirected to:

```text
/login
```

---

# 7. Logout

When the user clicks **Logout**, the application clears the session:

```python
session.clear()
```

The user is then redirected back to the login page.

---

# 🚀 Installation

## Step 1 — Install Python

Make sure Python is installed:

```powershell
python --version
```

Python 3.10 or newer is recommended.

---

## Step 2 — Open the Project

Open the project folder in **VS Code**.

Open the terminal:

```powershell
cd Secure_Login_System
```

---

## Step 3 — Create Virtual Environment

```powershell
python -m venv .venv
```

---

## Step 4 — Activate Virtual Environment

For Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

You should see:

```text
(.venv)
```

at the beginning of your terminal.

---

## Step 5 — Install Dependencies

Run:

```powershell
pip install -r requirements.txt
```

The required packages are:

```text
Flask
bcrypt
```

---

# ▶️ Run the Application

Start the Flask server:

```powershell
python app.py
```

You should see something similar to:

```text
* Running on http://127.0.0.1:5000
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

# 🧪 How to Test

## Test 1 — Registration

Open the application and click:

```text
Create one
```

Enter:

```text
Username: bibek
Email: bibek@example.com
Password: MyPassword123
```

Click:

```text
Create Account
```

You should see:

```text
Registration successful. Please log in.
```

---

## Test 2 — Login

Enter the same email and password.

If the credentials are correct:

```text
Login
   ↓
Session Created
   ↓
Dashboard
```

---

## Test 3 — Wrong Password

Try:

```text
Email: bibek@example.com
Password: wrongpassword
```

The application should display:

```text
Invalid email or password.
```

---

## Test 4 — Protected Dashboard

Without logging in, try opening:

```text
http://127.0.0.1:5000/dashboard
```

You should be redirected to the login page.

This demonstrates **protected route/session authentication**.

---

## Test 5 — Logout

After logging in, click:

```text
Logout
```

The session is cleared.

Trying to access `/dashboard` again should redirect you to the login page.

---

## Test 6 — SQL Injection

In the email field, try:

```text
' OR '1'='1
```

The application should **not** log you in.

This demonstrates the protection provided by parameterized SQL queries.

---

# 🗄️ Database

The project uses SQLite.

The database is created automatically at:

```text
instance/users.db
```

The `users` table contains:

```text
id
username
email
password_hash
created_at
```

Example:

```text
id:            1
username:      bibek
email:         bibek@example.com
password_hash: $2b$12$...
created_at:    2026-08-18 ...
```

Notice that the actual password is **not stored**.

---

# 📊 Expected Result

After successfully registering and logging in:

```text
┌──────────────────────────────┐
│      🔐 Secure Login         │
│                              │
│       ✓                      │
│                              │
│    Welcome, bibek!           │
│                              │
│  You are successfully        │
│  authenticated.              │
│                              │
│  Security Features           │
│  ✓ Bcrypt password hashing   │
│  ✓ Parameterized SQL         │
│  ✓ Input validation          │
│  ✓ Protected dashboard      │
│  ✓ Session logout            │
│                              │
│          [Logout]            │
└──────────────────────────────┘
```

---

# ⚠️ Limitations

This project is designed for **learning and internship demonstration**.

It is not yet a complete production authentication system.

Additional security features should be added before deploying it publicly.

---

# 🔮 Future Improvements

The following features can be added:

* [ ] Two-Factor Authentication (2FA)
* [ ] OTP verification
* [ ] Email verification
* [ ] Forgot password
* [ ] Password reset
* [ ] Login rate limiting
* [ ] Account lockout
* [ ] CSRF protection
* [ ] Secure cookies
* [ ] HTTPS
* [ ] Security headers
* [ ] Strong production secret key
* [ ] User profile page
* [ ] Admin dashboard
* [ ] Login activity tracking

---

# 🔐 Optional 2FA

A future version can add **Two-Factor Authentication** using TOTP.

The login process would become:

```text
Email + Password
       ↓
Password Correct?
       ↓
   Enter OTP
       ↓
OTP Correct?
   ↓       ↓
 Yes       No
  ↓         ↓
Dashboard  Reject
```

This provides an additional security layer even if a password is compromised.

---

# 🎓 Learning Outcomes

After completing this project, you will understand:

* How authentication works
* Password hashing
* Bcrypt
* Flask sessions
* Protected routes
* SQLite databases
* SQL injection prevention
* Input validation
* User registration
* Login authentication
* Logout/session management
* Basic web application security

---

# 👨‍💻 Author

**Bibek Thakur**

BTech – Computer Science
AITAM

---

# 📄 License

This project is created for **educational and internship purposes**.
