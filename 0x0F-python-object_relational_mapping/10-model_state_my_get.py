#!/usr/bin/python3
""" Query to show all the elements in the table """
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Table, Column


if __name__ == "__main__":
    ''' Select * from state '''
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]),
        pool_pre_ping=True
    )

    Base.metadata.bind = engine
    Session = sessionmaker()
    Session.bind = engine
    current_session = Session()
    result = current_session.query(State).filter(
        State.name == sys.argv[4]).one_or_none()
    if result:
        print(result.id)
    else:
        print('Not found')
