from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref
from .base import Base
from .session import session


class Coffee(Base):
    __tablename__ = "coffees"

    id = Column(Integer(), primary_key=True)
    roaster = Column(String(), index=True)
    name = Column(String())
    roast_level = Column(String(), index=True)

    ratings = relationship("Rating", backref=backref("Coffee"))

    def __repr__(self):
        return (
            f"Coffee #{self.id}: "
            + f"{self.roaster} {self.name}, "
            + f"a {self.roast_level} roast"
        )
