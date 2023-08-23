from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy import Column, DateTime, Integer, String

from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///beangrade.db")

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    def __repr__(self):
        return f"User #{self.id}: " + f"{self.name}"


class Coffee(Base):
    __tablename__ = "coffees"

    id = Column(Integer(), primary_key=True)
    roaster = Column(String(), index=True)
    name = Column(String())
    roast_level = Column(String(), index=True)
    date_received = Column(DateTime(), default=datetime.now)

    def __repr__(self):
        return (
            f"Coffee #{self.id}: "
            + f"{self.roaster} {self.name}, "
            + f"a {self.roast_level} roast received on {self.date_received}"
        )
