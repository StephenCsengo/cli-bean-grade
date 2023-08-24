from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref
from .base import Base
from .session import session


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

    @classmethod
    def add_new_user(cls, session, name):
        user = cls(name=name)

        session.add(user)
        session.commit()

    def __repr__(self):
        return f"User #{self.id}: " + f"{self.name}"
