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
        db = mysql.connector.connect(**config)
        print('\n Database user {} connected to MySQL on host {} with database {}'.format(config['user'],
                                                                                          config['host'],
                                                                                          config['database']))
        return db  # Return the database connection

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print(" The supplied username and password are invalid ")

        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("   The specified database does not exist")

        else:
            print(err)

# New function to display queries
def execute_query(db, query, description):
    cursor = db.cursor()
    cursor.execute(query)
    records = cursor.fetchall()

    print(f"\n----------------DISPLAYING {description} RECORDS--------------------")
    for record in records:
        for i in range(len(record)):
            print(f"{description} ID : {record[0]}\n{description} Name : {record[1]}\n")
            break

# Call the function
db = connect_to_mysql()

# Fetch data based on queries
if db:
    try:
        # The first and second query is to select all the fields for the studio and genre tables.
        scenario_1 = "SELECT * FROM studio;"
        execute_query(db, scenario_1, "Studio")

        scenario_2 = "SELECT * FROM genre;"
        execute_query(db, scenario_2, "Genre")

        # The third query is to select the movie names for those movies that have a run time of less than two hours
        scenario_3 = "SELECT film_name, film_runtime  FROM film WHERE film_runtime < 120;"
        execute_query(db, scenario_3, "Short Film")

        # The fourth query is to get a list of film names and directors ordered by director.
        scenario_4 = "SELECT film_name, film_director FROM film ORDER BY film_director;"
        execute_query(db, scenario_4, "Director")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        # Close the database connection
        db.close()
else:
    print("Failed to connect to the database.")
