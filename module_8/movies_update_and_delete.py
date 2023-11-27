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
def show_films(cursor, title):
    # Inner join statement for all tables
    cursor.execute("SELECT film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' FROM film "
                   "INNER JOIN genre ON film.genre_id = genre.genre_id INNER JOIN studio ON film.studio_id = studio.studio_id")

    # Result  from the cursor object
    films = cursor.fetchall()
    print("\n -- {} --".format(title))

    # Iterate Over the film the cursor object
    for film in films:
        print("Film Name :{}\nDirector: {}\nGenre Name: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))



# Call the function
db = connect_to_mysql()

# Fetch data based on queries
if db:
    try:
        # Display films before insert
        show_films(db.cursor(), "DISPLAYING FILMS BEFORE INSERT")

        # Insert a new record into the film table using a film of your choice. Do not use 'Star Wars'. (Easier if you use a studio already in use..)

        insert_query = "INSERT INTO film (film_id, film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        insert_data = (4, "Joy", 2015, 124, "David O. Russell", 3, 1)  # 3 is the Drama genre_id, and 1 is the studio_id
        db.cursor().execute(insert_query, insert_data)
        db.commit()

        # Display films after insert
        show_films(db.cursor(), "DISPLAYING FILMS AFTER INSERT")

        # Update the film Alien to being a Horror film
        update_query = "UPDATE film SET genre_id = 1 WHERE film_name = 'Alien' "
        db.cursor().execute(update_query)
        db.commit()

        # Display films after update
        show_films(db.cursor(), "DISPLAYING FILMS AFTER UPDATE- Changed Alien to Horror")

        # Delete the movie Gladiator
        delete_query = "DELETE FROM film WHERE film_name = 'Gladiator'"
        db.cursor().execute(delete_query)
        db.commit()

        # Display films after delete
        show_films(db.cursor(), "DISPLAYING FILMS AFTER DELETE")



    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        # Close the database connection
        db.close()
else:
    print("Failed to connect to the database.")
