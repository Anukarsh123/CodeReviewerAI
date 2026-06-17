from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Create users table automatically
def create_table():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        password TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()

create_table()


# Login Page
@app.route("/")
def login():
    return render_template("login.html")


# Register Page
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
            (username, email, password)
        )

        conn.commit()
        conn.close()

        return redirect("/")

    return render_template("register.html")


# Dashboard
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# Review Page
@app.route("/review", methods=["GET", "POST"])
def review():

    result = ""

    if request.method == "POST":

        code = request.form.get("code", "")

        if "password" in code.lower():
            result += "⚠ Hardcoded password detected.<br>"

        if "print(" in code:
            result += "ℹ Debug print statement found.<br>"

        if "for" in code and code.count("for") > 1:
            result += "⚠ Nested loop detected. May affect performance.<br>"

        if result == "":
            result = "✅ No major issues found."

    return render_template("review.html", result=result)


# History Page
@app.route("/history")
def history():
    return render_template("history.html")


if __name__ == "__main__":
    app.run(debug=True)
