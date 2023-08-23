#!/usr/bin/env python3
"""
Script to list all State objects containing the letter "a" from 
a MySQL database using SQLAlchemy
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>".format(
            sys.argv[0]))
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create an engine to connect to the MySQL server
    engine_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        mysql_username, mysql_password, database_name)
    engine = create_engine(engine_url)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and print State objects containing the letter "a" in
    #  ascending order by states.id
    states_with_a = session.query(State).filter(
        State.name.like('%a%')).order_by(State.id).all()
    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))

    session.close()
