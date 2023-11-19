import mysql.connector
from mysql.connector import connection


def connect_to_mysql():
    config = {
        'user': 'root',
        'password': 'Bennington@1',
        'host': '127.0.0.1',
        'database': 'movies',
        'raise_on_warnings': True
    }

    try:
        db = mysql.connector.connect(**config)
        print('\n Database user {} connected to MySQL on host {}')

        if db.is_connected():
            print("Connected to MySQL database")
            return db
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return None



