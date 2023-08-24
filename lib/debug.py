#!/usr/bin/env python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import User, Coffee, Rating

if __name__ == "__main__":
    engine = create_engine("sqlite:///db/beangrade.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    import ipdb

    ipdb.set_trace()
