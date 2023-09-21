# Israel Microgreens API and User Interface

This is a simple project that creates a RESTful API to interact with a relational database, providing two endpoints: one to retrieve a list of Microgreens and their prices, and the other to retrieve a list of customers and the amount of Microgreens they have ordered. The database tables are normalized, and SQL joins are used to fetch the required data. The API responses are in JSON format. Additionally, a user interface is created to fetch and display the data in a tabular format.

## Table of Contents
- [Project Description](#israel-microgreens-api-and-user-interface)
- [How to Run](#how-to-run)
- [API Endpoints](#api-endpoints)
- [Database Architecture](#database-architecture)
- [User Interface](#user-interface)

## How to Run

Follow these steps to set up and run the Israel Microgreens API and User Interface:

1. **Pull the MySQL Docker Image:**
   ```
   docker pull mysql
   ```

2. **Run the MySQL Docker Container:**
   ```
   docker run -d -p 3306:3306 --name mysql-container -e MYSQL_ROOT_PASSWORD=q1w2e3r4 mysql:latest
   ```

3. **Clone the Repository:**
   ```
   git clone https://github.com/noahweiss890/Israel-Microgreens-Project.git
   cd Israel-Microgreens-Project
   ```

4. **Initialize the Database and Define Tables:**
   ```
   python3 init_sql_db.py
   ```

5. **Start the Microgreen API:**
   ```
   python3 microgreen_api.py
   ```

6. **Start the Microgreen Node Server:**
   ```
   cd microgreen_node && npm start
   ```

7. **Open Your Browser and Go to:**
   ```
   http://localhost:3000
   ```

## API Endpoints

The Israel Microgreens API provides the following API endpoints:

1. **Retrieve Microgreens and Prices**
   - **Endpoint:** `/microgreens`
   - **Method:** GET
   - **Description:** Returns a list of Microgreens and their prices in JSON format.

2. **Retrieve Customers and Ordered Microgreens**
   - **Endpoint:** `/customers`
   - **Method:** GET
   - **Description:** Returns a list of customers and the amount of Microgreens they have ordered in JSON format.

## Database Architecture

The database architecture of this project is designed to be normalized for efficient data storage and retrieval. It includes tables for Microgreens, Customers, and Orders. The relationships between these tables are established through foreign keys, and SQL joins are used in API queries to fetch relevant data.

## User Interface

A user interface is created to interact with the Israel Microgreens Database. You can access this interface by opening your web browser and navigating to [http://localhost:3000](http://localhost:3000). The interface allows you to view the data, presenting it in a clear and user-friendly tabular format.

## Technologies Used

This project leverages the following technologies to deliver its functionality:

- **Python:** Used for backend development, database initialization, and API implementation.
- **Node.js:** Employed for the Microgreen Node Server, enhancing the system's performance and scalability.
- **MySQL:** A relational database management system utilized for data storage and retrieval.
- **Docker:** Used to containerize the MySQL database for easy deployment.
- **HTML/CSS/JavaScript:** These web technologies are employed to create the user interface.
- **Git:** Version control system for collaborative development and code management.
