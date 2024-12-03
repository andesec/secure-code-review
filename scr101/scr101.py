import sqlite3, hashlib

from flask import Flask, request, render_template_string

app = Flask(__name__)


# Database setup
def setup_database():
    connection = sqlite3.connect("scr101.db")
    cursor = connection.cursor()

    # Create users table
    cursor.execute("DROP TABLE IF EXISTS users")
    cursor.execute(
        """
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL
        )
    """
    )

    # Insert sample users with hashed passwords
    users = [
        ('admin', hashlib.sha256(b'admin123').hexdigest()),
        ('user1', hashlib.sha256(b'userpass').hexdigest())
    ]
    cursor.executemany("INSERT INTO users (username, password_hash) VALUES (?, ?)", users)
    connection.commit()
    connection.close()


# Vulnerable login function
@app.route('/', methods=['GET', 'POST'])
def login():
    form_html = """
    <h3>Login</h3>
    <form method="POST">
        <label>Username:</label>
        <input type="text" name="username"><br>
        <label>Password:</label>
        <input type="password" name="password"><br>
        <button type="submit">Login</button>
    </form>
    <div style="color: red;">MESSAGE</div>
    """
    message = ""

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # SQL Injection vulnerability here
        connection = sqlite3.connect("scr101.db")
        cursor = connection.cursor()

        # Problem: User input is directly included in the query string without sanitization
        query = f"SELECT * FROM users WHERE username = '{username}'"
        print(f"Executing query: {query}")  # Debugging output
        cursor.execute(query)
        user = cursor.fetchone()
        connection.close()

        if user:
            stored_hash = user[2]  # Retrieve hashed password from database
            if hashlib.sha256(password.encode('utf-8')).hexdigest() == stored_hash:
                message = f"Login successful for {user[1]}!"
            else:
                message = "Invalid password. Try again."
        else:
            message = "Invalid username. Try again."

    return render_template_string(form_html.replace("MESSAGE", message))


if __name__ == '__main__':
    setup_database()  # Initialize the database
    app.run(debug=True)
