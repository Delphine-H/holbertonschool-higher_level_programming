#!/usr/bin/python3
import MySQLdb
import sys

# Check if correct number of arguments are provided
if len(sys.argv) != 5:
    print("Usage: {} username password database state_name"
          .format(sys.argv[0]))
    sys.exit(1)

# Capture command line arguments
username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]
state_name = sys.argv[4]

# Connect to MySQL database
db = MySQLdb.connect(
    host="localhost",
    port=3306,
    user=username,
    passwd=password,
    db=database
)

# Create a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to retrieve states matching the provided state_name
sql_query = "SELECT * FROM states WHERE name LIKE BINARY '{}'".format(argv[4])

# Execute the SQL command with the state_name as parameter
cursor.execute(sql_query, (state_name,))

# Fetch all the rows in a list of tuples
results = cursor.fetchall()

# Print the results in the required format
for row in results:
    print(row)

# Disconnect from server
cursor.close()
db.close()
