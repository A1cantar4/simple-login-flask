# SIMPLE LOGIN SYSTEM

A simple Flask-based web application with basic user authentication.

## Purpose

The purpose of this project is to practice creating a basic login system using the Flask framework, handling forms, routes, and basic HTML templates.

## Technologies & Languages Used

- Python  
- HTML  
- Flask  
- Jinja2 (template engine used by Flask)

- Structure: English
- For final user: Portuguese

## Features

- Basic username and password authentication  
- HTML templates with conditional rendering (e.g., error messages)  
- Redirection after successful login  
- Clear code structure, easy to expand in the future (e.g., adding database/SQL support)

## File Structure

```
simple-login-system/
│
├── app.py                   # Main Flask application
├── templates/
│   ├── login.html           # Login form
│   └── welcome.html         # Success page
├── requirements.txt         
├── .gitignore               # (¬_¬) For our security
└── README.md                # Project documentation
```

## How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/seu-usuario/simple-login-system.git
   cd simple-login-system
   ```

2. (Optional but recommended) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. Install Requirements:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the app:
   ```bash
   python app.py
   ```

5. Access it in your browser at:
   ```
   http://127.0.0.1:5000
   ```

## Author

- [@A1cantar4](https://github.com/A1cantar4)
