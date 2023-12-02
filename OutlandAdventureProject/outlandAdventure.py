import mysql.connector
from mysql.connector import errorcode

# Database configuration
config = {
    'user': 'root',
        'password': 'Bennington@1',
        'host': '127.0.0.1',
        'database': 'OutlandAdventures',
        'raise_on_warnings': True
}

db = None  # Initialize db variable outside the try block

try:
    # Establishing a connection to the database
    db = mysql.connector.connect(**config)
    print("\nDatabase user {} connected to MYSQL on host {} with database {}".format(config["user"], config["host"],
                                                                                      config["database"]))
    input("\n\nPress enter to continue...\n")

    cursor = db.cursor()

    # Displaying Customer Table
    cursor.execute("SELECT name, destination, equipUsed, equipStatus FROM customer")
    customers = cursor.fetchall()
    print("Displaying Customer Table")
    for customer in customers:
        print("Name: {}\nDestination: {}\nUsed Equipment: {}\nEquipment Status: {}\n".format(customer[0], customer[1],
                                                                                             customer[2], customer[3]))

    # Displaying Equipment Table
    cursor.execute("SELECT equipmentName, equipmentType, acquisitionDate FROM equipment")
    equipment = cursor.fetchall()
    print("Displaying Equipment Table")
    for eq in equipment:
        print("Equipment: {}\nType: {}\nDate: {}\n".format(eq[0], eq[1], eq[2]))

    # Displaying Outland Adventure Guides
    cursor.execute("SELECT name FROM guide")
    guides = cursor.fetchall()
    print("Displaying Outland Adventure Guides")
    for guide in guides:
        print("Name: {}\n".format(guide[0]))

    # Displaying Destination Table
    cursor.execute("SELECT continent, region, startDate, endDate FROM destination")
    destinations = cursor.fetchall()
    print("Displaying Destination Table")
    for destination in destinations:
        print("Continent: {}\nRegion: {}\nBeginning Date {}\nEnd Date {}\n".format(destination[0], destination[1],
                                                                                   destination[2], destination[3]))


except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password is invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")

    else:
        print(err)

finally:
    if db is not None:
        db.close()