from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret-key'
app.config['DB_PASSWORD'] = 'db-password'
app.config['DB_HOST'] = 'mysql'
app.config['DB_USER'] = 'root'
app.config['DB_NAME'] = 'scrpy01'

@app.route('/',  methods=['GET'])
def home():
    return jsonify({
        "message": "SCRPY01 - This is a secure code review example."
    })

@app.route('/data',  methods=['GET'])
def get_data():
    connection = mysql.connector.connect(
        host=app.config['DB_HOST'],
        user=app.config['DB_USER'],
        password=app.config['DB_PASSWORD'],
        database=app.config['DB_NAME']
    )
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM data")
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
