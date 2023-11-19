import mysql.connector
from mysql.connector import errorcode

def connect_to_mysql():
    config = {
        'user': 'root',
        'password': 'Bennington@1',
        'host': '127.0.0.1',
        'database': 'movies',
        'raise_on_warnings': True
    }

    try:
        with mysql.connector.connect(**config) as db:
            print('\n Database user {} connected to MySQL on host {} with database {}'.format(config['user'],
                                                                                              config['host'],
                                                                                              config['database']))
            input('\n\n Press any key to continue...............')

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print(" The supplied username and password are invalid ")

        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("   The specified database does not exist")

        else:
            print(err)


# Call the function
connect_to_mysql()
