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

    user = relationship("User", backref=backref("User"))
    coffee = relationship("Coffee", backref=backref("Coffee"))

    def __repr__(self):
        return (
            f"Rating\n"
            + f"id = {self.id}"
            + f"user_id = {self.user_id}"
            + f"user_name = {self.user.name}"
            + f"coffee_id = {self.coffee}"
            + f"rating = {self.rating}"
        )
