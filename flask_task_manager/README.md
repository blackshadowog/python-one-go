# TaskFlow - Flask Task Manager

A complete mini project built with Python Flask and SQLite.

## Features

- User registration and login
- Session-based authentication
- Personal task dashboard
- Add tasks
- Complete / undo tasks
- Delete tasks
- SQLite database
- Responsive HTML/CSS UI
- Flash messages

## Project Structure

```text
flask_task_manager/
├── app.py
├── requirements.txt
├── README.md
├── tasks.db              # created automatically
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   └── dashboard.html
└── static/
    └── style.css
```

## Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Start the app

```bash
python app.py
```

### 3. Open

```text
http://127.0.0.1:5000
```

## Note

This is an educational project. For production use, passwords should be hashed with Werkzeug or another secure password-hashing system, and the Flask secret key should be stored securely.
