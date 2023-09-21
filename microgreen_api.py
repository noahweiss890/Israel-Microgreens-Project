from flask import Flask, jsonify, render_template
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Database Connection
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "q1w2e3r4",
    "database": "israelmicrogreens",
}

# Endpoint for home page
@app.route("/")
def home():
    return "<h1>Welcome to Israel Microgreens!</h1>"


# Endpoint to get Microgreens and prices
@app.route("/microgreens", methods=["GET"])
def get_microgreens():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT name, price FROM Microgreens")
    microgreens = cursor.fetchall()
    conn.close()
    return jsonify(microgreens)


# Endpoint to get Customers and the amount of Microgreens ordered
@app.route("/customers", methods=["GET"])
def get_customers():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT Customers.name, Customers.phone, SUM(Orders.quantity) AS total_ordered
        FROM Customers JOIN Orders
        ON Customers.id = Orders.customer_id
        GROUP BY Customers.id
    """)
    customers = cursor.fetchall()
    conn.close()
    return jsonify(customers)


if __name__ == "__main__":
    app.run(debug=True)
