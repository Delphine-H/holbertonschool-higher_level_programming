#!/usr/bin/python3
"""Prints the first State object from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    # Connect to MySQL server
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)

    # Bind the engine to the Base class
    Base.metadata.bind = engine

    # Create a session maker
    DBSession = sessionmaker(bind=engine)

    # Create a session
    session = DBSession()

    # Query the first State object ordered by id
    first_state = session.query(State).order_by(State.id).first()

    # Check if result is None
    if first_state is None:
        print("Nothing")
    else:
        # Print the result in the required format
        print("{}: {}".format(first_state.id, first_state.name))

    # Close the session
    session.close()
