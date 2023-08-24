from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship, backref
from .base import Base
from .session import session


class Rating(Base):
    __tablename__ = "ratings"

    id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), ForeignKey("users.id"))
    coffee_id = Column(Integer(), ForeignKey("coffees.id"))
    rating = Column(Integer(), index=True)

    users = relationship("User", backref=backref("User"))
    coffees = relationship("Coffee", backref=backref("Coffee"))

    def __repr__(self):
        return (
            f"Rating #{self.id}: "
            + f"Coffee #{self.coffee_id} by {self.user_id}"
            + f"Rating of {self.rating}"
        )
