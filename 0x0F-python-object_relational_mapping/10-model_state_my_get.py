#!/usr/bin/python3
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import create_engine
from sys import argv

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == argv[4]).first()

    if state is None:
        print('Not found')
    else:
        print('{}'.format(state.id))
