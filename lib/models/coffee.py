from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship, backref
from .base import Base
from .session import session
from datetime import datetime


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
