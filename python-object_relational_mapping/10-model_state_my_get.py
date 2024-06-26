#!/usr/bin/python3
"""
Prints the State object with
the name passed as argument
from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} username password database state_name"
              .format(sys.argv[0]))
        sys.exit(1)

    username, password, database, state_name = \
        sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    # Connect to MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database), echo=False)

    # Bind the engine to the Base class
    Base.metadata.bind = engine

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for the State object by name
    state = session.query(State).filter(State.name == state_name).first()

    # If state is found, print its id; otherwise, print "Not found"
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()
