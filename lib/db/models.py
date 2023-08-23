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
