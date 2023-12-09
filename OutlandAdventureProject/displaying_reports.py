import mysql.connector
from mysql.connector import errorcode
from datetime import datetime, timedelta

# Database configuration
config = {
    'user': 'outland_user',
    'password': 'adventure',
    'host': '127.0.0.1',
    'database': 'Outland Adventures',
    'raise_on_warnings': True
}

db = None  # Initialize db variable outside the try block

try:
    # Establishing a connection to the database
    db = mysql.connector.connect(**config)
    print("\n Database user {} connected to MYSQL on host {} with database {}".format(config["user"], config["host"],
                                                                                       config["database"]))
    input("\n\n Press enter to continue...\n")

    cursor = db.cursor()

    # Report #1: Percentage of customers who purchased equipment VS rent
    cursor.execute("SELECT COUNT(*) as 'TotalCustomers', SUM(CASE WHEN equipStatus = 'Purchase' THEN 1 ELSE 0 END) as 'PurchasedCustomers', SUM(CASE WHEN equipStatus = 'Rental' THEN 1 ELSE 0 END) as 'RentedCustomers' FROM customer")
    result = cursor.fetchone()
    total_customers = result[0]
    purchased_customers = result[1]
    rented_customers = result[2]
    percent_purchased = (purchased_customers / total_customers) * 100
    percent_rented = (rented_customers / total_customers) * 100

    print("QUERYING FOR PERCENTAGE OF EQUIPMENT PURCHASE VS RENTAL")
    print("{:.2f}% of customers have purchased equipment.".format(percent_purchased))
    print("{:.2f}% of customers have rented equipment.".format(percent_rented))
    # Report #2: Percentage of bookings for each destination
    cursor.execute("SELECT destination.continent, COUNT(*) as 'Bookings' FROM customer INNER JOIN destination ON customer.destination = destination.destinationID GROUP BY destination.continent")
    results = cursor.fetchall()
    print("\n==DISPLAYING CUSTOMERS AND THEIR BOOKED DESTINATIONS==")
    for row in results:
        continent, bookings = row
        percent_bookings = (bookings / total_customers) * 100
        print("The percentage of bookings for {} is {:.2f}%.".format(continent, percent_bookings))

    # Report #3: Equipment over 5 years old
    cursor.execute("SELECT equipmentName as 'Equipment', acquisitionDate as 'Acquired' FROM equipment")
    equip_date = cursor.fetchall()

    print("\n==DISPLAYING EQUIPMENT AND THEIR ACQUISITION DATE==")
    for equip in equip_date:
        print(equip)

    # Filter out equipment over 5 years old
    current_date = datetime.today()
    five_years_ago = current_date - timedelta(days=5 * 365)  # Assuming a year has 365 days

    old_equipment = [equip for equip in equip_date if datetime.strptime(str(equip[1]), '%Y-%m-%d') < five_years_ago]

    print("\n==DISPLAYING EQUIPMENT OVER 5 YEARS OLD==")
    for equip in old_equipment:
        print(equip)

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password is invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")

    else:
        print(err)

finally:
    db.close()