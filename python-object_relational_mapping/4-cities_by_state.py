#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Capture command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        # Connect to MySQL database
        db = MySQLdb.connect(
            host="localhost", port=3306, user=username,
            passwd=password, db=database
        )

        # Create a cursor object using cursor() method
        cursor = db.cursor()

        # Prepare SQL query to retrieve cities with state names
        sql_query = """
            SELECT cities.id, cities.name, states.name
            FROM cities
            INNER JOIN states ON cities.state_id = states.id
            ORDER BY cities.id ASC
        """

        # Execute the SQL command
        cursor.execute(sql_query)

        # Fetch all rows from the result set
        results = cursor.fetchall()

        # Print the results in the required format
        for row in results:
            print(row)

    except MySQLdb.Error as e:
        print("MySQLdb Error:", e)

    finally:
        # Disconnect from server
        if 'db' in locals() and db:
            cursor.close()
            db.close()
