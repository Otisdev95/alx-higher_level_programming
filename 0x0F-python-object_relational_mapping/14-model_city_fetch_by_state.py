#!/usr/bin/python3
"""
    Python file similar to model_state.py named model_city.py
    that contains the class definition of a City.
    Script 14-model_city_fetch_by_state.py that prints all City
    objects from the database hbtn_0e_14_usa:
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
        Accesses to the database and get the cities
        from the database
    """

    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            argv[1], argv[2], argv[3])

    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)

    session = Session()
    outcome = session.query(City, State).join(State)

    for city, state in outcome.all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.commit()
    session.close()
