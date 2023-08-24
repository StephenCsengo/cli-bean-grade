from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy import ForeignKey, Column, DateTime, Integer, String
from sqlalchemy.orm import relationship, backref, sessionmaker

from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

engine = create_engine("sqlite:///db/beangrade.db")
Session = sessionmaker(bind=engine)
session = Session()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    ratings = relationship("Rating", backref=backref("User"))

    @classmethod
    def find_by_name(cls, name):
        user = session.query(cls).get(name)
        if user:
            return user
        else:
            return "No user found!"

    def __repr__(self):
        return f"User #{self.id}: " + f"{self.name}"


class Coffee(Base):
    __tablename__ = "coffees"

    id = Column(Integer(), primary_key=True)
    roaster = Column(String(), index=True)
    name = Column(String())
    roast_level = Column(String(), index=True)
    date_received = Column(DateTime(), default=datetime.now, index=True)

    ratings = relationship("Rating", backref=backref("Coffee"))

    def __repr__(self):
        return (
            f"Coffee #{self.id}: "
            + f"{self.roaster} {self.name}, "
            + f"a {self.roast_level} roast received on {self.date_received}"
        )


class Rating(Base):
    __tablename__ = "ratings"

    id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), ForeignKey("users.id"))
    coffee_id = Column(Integer(), ForeignKey("coffees.id"))
    rating = Column(Integer(), index=True)

    def __repr__(self):
        return (
            f"Rating #{self.id}: "
            + f"Coffee #{self.coffee_id} by {self.user_id}"
            + f"Rating of {self.rating}"
        )
