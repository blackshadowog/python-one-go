from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
from functools import wraps
from pathlib import Path

app = Flask(__name__)
app.secret_key = "change-this-secret-key"
DB = Path("tasks.db")

def get_db():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_db() as db:
        db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        """)
        db.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                title TEXT NOT NULL,
                description TEXT DEFAULT '',
                status TEXT DEFAULT 'Pending',
                FOREIGN KEY(user_id) REFERENCES users(id)
            )
        """)
        db.commit()

def login_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("login"))
        return fn(*args, **kwargs)
    return wrapper

@app.route("/")
def index():
    if "user_id" in session:
        return redirect(url_for("dashboard"))
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"]

        if not username or not password:
            flash("Username and password are required.")
            return redirect(url_for("register"))

        try:
            with get_db() as db:
                db.execute(
                    "INSERT INTO users(username, password) VALUES (?, ?)",
                    (username, password)
                )
                db.commit()
            flash("Account created. Please login.")
            return redirect(url_for("login"))
        except sqlite3.IntegrityError:
            flash("Username already exists.")

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"]

        with get_db() as db:
            user = db.execute(
                "SELECT * FROM users WHERE username=? AND password=?",
                (username, password)
            ).fetchone()

        if user:
            session["user_id"] = user["id"]
            session["username"] = user["username"]
            return redirect(url_for("dashboard"))

        flash("Invalid username or password.")

    return render_template("login.html")

@app.route("/dashboard")
@login_required
def dashboard():
    with get_db() as db:
        tasks = db.execute(
            "SELECT * FROM tasks WHERE user_id=? ORDER BY id DESC",
            (session["user_id"],)
        ).fetchall()

    total = len(tasks)
    completed = sum(t["status"] == "Completed" for t in tasks)
    pending = total - completed

    return render_template(
        "dashboard.html",
        tasks=tasks,
        total=total,
        completed=completed,
        pending=pending
    )

@app.route("/task/add", methods=["POST"])
@login_required
def add_task():
    title = request.form["title"].strip()
    description = request.form.get("description", "").strip()

    if title:
        with get_db() as db:
            db.execute(
                "INSERT INTO tasks(user_id, title, description) VALUES (?, ?, ?)",
                (session["user_id"], title, description)
            )
            db.commit()

    return redirect(url_for("dashboard"))

@app.route("/task/<int:task_id>/toggle")
@login_required
def toggle_task(task_id):
    with get_db() as db:
        task = db.execute(
            "SELECT status FROM tasks WHERE id=? AND user_id=?",
            (task_id, session["user_id"])
        ).fetchone()

        if task:
            new_status = "Pending" if task["status"] == "Completed" else "Completed"
            db.execute(
                "UPDATE tasks SET status=? WHERE id=? AND user_id=?",
                (new_status, task_id, session["user_id"])
            )
            db.commit()

    return redirect(url_for("dashboard"))

@app.route("/task/<int:task_id>/delete")
@login_required
def delete_task(task_id):
    with get_db() as db:
        db.execute(
            "DELETE FROM tasks WHERE id=? AND user_id=?",
            (task_id, session["user_id"])
        )
        db.commit()

    return redirect(url_for("dashboard"))

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
