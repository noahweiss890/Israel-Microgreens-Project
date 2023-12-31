import mysql.connector

# Database Connection
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "q1w2e3r4",
    "database": "israelmicrogreens",
}


# Function to add a new Microgreen entry
def add_microgreen(name, price):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Insert into Microgreens table
        insert_query = "INSERT INTO Microgreens (name, price) VALUES (%s, %s)"
        data = (name, price)
        cursor.execute(insert_query, data)

        connection.commit()
        print(f"Added Microgreen: {name} - Price: {price}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()


# Function to add a new Customer entry
def add_customer(name, phone):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Insert into Customers table
        insert_query = "INSERT INTO Customers (name, phone) VALUES (%s, %s)"
        data = (name, phone)
        cursor.execute(insert_query, data)

        connection.commit()
        print(f"Added Customer: {name} - Phone: {phone}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()


# Function to add a new Order entry
def add_order(customer_id, microgreen_id, quantity):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Insert into Orders table
        insert_query = "INSERT INTO Orders (customer_id, microgreen_id, quantity) VALUES (%s, %s, %s)"
        data = (customer_id, microgreen_id, quantity)
        cursor.execute(insert_query, data)

        connection.commit()
        print(f"Added Order: Customer ID: {customer_id} - Microgreen ID: {microgreen_id} - Quantity: {quantity}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":

    # Adding Microgreens:
    add_microgreen("Broccoli", 25)
    add_microgreen("Kale", 25)
    add_microgreen("Purple Radish", 25)
    add_microgreen("China Rose Radish", 25)
    add_microgreen("Sunflower", 25)
    add_microgreen("Pea", 25)
    add_microgreen("Mustard", 25)
    add_microgreen("Amaranth", 30)

    # Adding Customers:
    add_customer("David Melech", "0501234567")
    add_customer("Moshe Odin", "0522345678")
    add_customer("Avi Agami", "0533456789")
    add_customer("Shira Racheli", "0544567890")
    add_customer("Roni Shirazi", "0559876543")
    add_customer("Yael Shaked", "0568765432")

    # Adding Orders:
    add_order(1, 1, 2)
    add_order(1, 3, 3)
    add_order(1, 6, 1)

    add_order(2, 8, 1)
    add_order(2, 1, 7)
    add_order(2, 7, 2)

    add_order(3, 2, 1)
    add_order(3, 4, 2)

    add_order(4, 1, 1)
    add_order(4, 4, 4)

    add_order(5, 5, 3)
    add_order(5, 6, 1)

    add_order(6, 7, 2)
    add_order(6, 8, 1)
