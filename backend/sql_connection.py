import os
import mysql.connector
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

__cnx = None

def get_sql_connection():
    """
    Establish and return a MySQL database connection.
    Reads connection details from environment variables.
    """
    print("Opening MySQL connection")
    global __cnx

    if __cnx is None:
        try:
            # Establish the MySQL connection
            __cnx = mysql.connector.connect(
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                host=os.getenv("DB_HOST", "localhost"),  # Default to localhost if not set
                database=os.getenv("DB_NAME")
            )
            print("MySQL connection established successfully.")
        except mysql.connector.Error as err:
            print(f"Error connecting to MySQL: {err}")
            raise  # Rethrow the exception for the caller to handle
    return __cnx
