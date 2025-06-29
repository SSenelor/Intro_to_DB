import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        # Connect to MySQL server (adjust user, password, host as needed)
        conn = mysql.connector.connect(
            user='root',
            password='your_password',
            host='localhost'
        )
        cursor = conn.cursor()

        # SQL statement to create the database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print("Error: Unable to connect to the database.")
        print(f"MySQL Error: {err}")

    finally:
        # Close cursor and connection if they exist
        try:
            cursor.close()
            conn.close()
        except:
            pass

if __name__ == "__main__":
    create_database()
