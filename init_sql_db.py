import mysql.connector

# Database Connection
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "q1w2e3r4",
}

# Create a new database
def create_database(cursor):
    cursor.execute("CREATE DATABASE IF NOT EXISTS israelmicrogreens")  # Replace with your desired database name

# Create Microgreens table
def create_microgreens_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Microgreens (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            price DECIMAL(10, 2) NOT NULL
        )
    """)

# Create Customers table
def create_customers_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Customers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            phone VARCHAR(10) NOT NULL
        )
    """)

# Create Orders table
def create_orders_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Orders (
            id INT AUTO_INCREMENT PRIMARY KEY,
            customer_id INT,
            microgreen_id INT,
            quantity INT,
            FOREIGN KEY (customer_id) REFERENCES Customers(id),
            FOREIGN KEY (microgreen_id) REFERENCES Microgreens(id)
        )
    """)


if __name__ == "__main__":
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Create the database
        create_database(cursor)

        # Switch to the newly created database
        cursor.execute("USE israelmicrogreens")

        # Create Microgreens table
        create_microgreens_table(cursor)

        # Create Customers table
        create_customers_table(cursor)

        # Create Orders table
        create_orders_table(cursor)

        print("Database and tables created successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()
        
