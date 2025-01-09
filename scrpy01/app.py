from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# Configuration (intentionally insecure)
app.config['SECRET_KEY'] = 'secret-key'
app.config['DB_PASSWORD'] = 'db-password'
app.config['DB_HOST'] = 'mysql'
app.config['DB_USER'] = 'root'
app.config['DB_NAME'] = 'insecure_db'

@app.route('/')
def home():
    return jsonify({
        "message": "This is a Python secure code review example."
    })

@app.route('/data')
def get_data():
    connection = get_conn()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM data")
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(result)

def get_conn():
    return mysql.connector.connect(
        host=app.config['DB_HOST'],
        user=app.config['DB_USER'],
        password=app.config['DB_PASSWORD'],
        database=app.config['DB_NAME']
    )

def setup_db():
    connection = get_conn()
    cursor = connection.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {app.config['DB_NAME']}")
    cursor.execute(f"USE {app.config['DB_NAME']}")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS data (
            id INT AUTO_INCREMENT PRIMARY KEY,
            value VARCHAR(255)
        )
    """)
    cursor.execute("INSERT INTO data (value) VALUES ('sample')")
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == '__main__':
    setup_db()  # Initialize the database
    app.run(debug=True)
