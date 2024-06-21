#!/usr/bin/python3
"""
Lists all State objects that contain
the letter 'a' from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database), echo=False)

    # Bind the engine to the Base class
    Base.metadata.bind = engine

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query State objects containing letter 'a'
    results = session.query(State).filter(State.name.like('%a%'))
    .order_by(State.id).all()

    # Print results in required format
    for state in results:
