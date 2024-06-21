#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Check if correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    # Capture command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL database
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
    except MySQLdb.Error as e:
        print("Error connecting to MySQL:", e)
        sys.exit(1)

    # Create a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to retrieve states starting with 'N'
    sql_query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"

    try:
        # Execute the SQL command
        cursor.execute(sql_query)

        # Fetch all the rows in a list of tuples
        results = cursor.fetchall()

        # Print the results
        for row in results:
            print(row)

    except MySQLdb.Error as e:
        print("Error retrieving data from MySQL:", e)
        sys.exit(1)

    # Disconnect from server
    db.close()
