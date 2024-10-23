import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Establishing connection to MySQL server
        connection = mysql.connector.connect(
            host='localhost',  # Update to your MySQL server host
            user='root',       # Update with your MySQL username
            password='yourpassword'  # Update with your MySQL password
        )

        if connection.is_connected():
            # Creating a cursor to execute MySQL commands
            cursor = connection.cursor()
            # Creating the alx_book_store database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
    
    except mysql.connector.Error as err:
        print(f"Error: '{err}' occurred while connecting to MySQL")
    
    finally:
        # Closing the database connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    create_database()
