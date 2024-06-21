#!/usr/bin/python3
"""
Script that lists all cities of a given state from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Capture command line arguments
    if len(sys.argv) != 5:
        print("Usage: {} username password database state_name"
              .format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL database
    db = MySQLdb.connect(
        host="localhost", port=3306, user=username,
        passwd=password, db=database
    )

    cursor = db.cursor()

    # Prepare SQL query to retrieve cities of the specified state
    sql_query = """
        SELECT GROUP_CONCAT(cities.name SEPARATOR ', ')
        FROM cities
        INNER JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
        """

    # Execute the SQL command with state_name as parameter
    cursor.execute(sql_query, (state_name,))

    # Fetch the first row from the result set
    result = cursor.fetchone()

    if result:
        # Print the results in the required format
        print(result[0])

    # Clean up
    cursor.close()
    db.close()
