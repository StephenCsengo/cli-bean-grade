from sqlalchemy import create_engine
from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship, backref, declarative_base, sessionmaker


Base = declarative_base()
engine = create_engine("sqlite:///db/beangrade.db")
Session = sessionmaker(bind=engine)
session = Session()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    @classmethod
    def find_by_name(cls, name):
        user_search = session.query(User).filter(User.name.like(name)).first()
        if user_search:
            return user_search
        else:
            return None

    @classmethod
    def add_new_user(cls, name):
        user = cls(name=name)
        session.add(user)
        session.commit()
        print(f"User {name} created.")

    def __repr__(self):
        return f"User #{self.id}: " + f"{self.name}"


class Coffee(Base):
    __tablename__ = "coffees"

    id = Column(Integer(), primary_key=True)
    roaster = Column(String(), index=True)
    name = Column(String())
    roast_level = Column(String(), index=True)

    @classmethod
    def add_new_coffee(cls, roaster, name, roast_level):
        coffee = cls(roaster=roaster, name=name, roast_level=roast_level)
        session.add(coffee)
        session.commit()
        print(f"{coffee} add to database.")

    @classmethod
    def find_by_id(cls, coffee_id):
        coffee_id_search = (
            session.query(Coffee).filter(Coffee.id.like(coffee_id)).first()
        )
        return coffee_id_search

    def __repr__(self):
        return (
            f"Coffee #{self.id}: "
            + f"{self.roaster} {self.name}, "
            + f"a {self.roast_level} roast"
        )


class Rating(Base):
    __tablename__ = "ratings"

    id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), ForeignKey("users.id"))
    coffee_id = Column(Integer(), ForeignKey("coffees.id"))
    rating = Column(Integer(), index=True)

    user = relationship("User", backref=backref("User"))
    coffee = relationship("Coffee", backref=backref("Coffee"))

    @classmethod
    def add_new_rating(cls, user_id, coffee_id):
        rating = input("Rate this coffee 1-10: ")
        new_rating = Rating(user_id=user_id, coffee_id=coffee_id, rating=rating)
        session.add(new_rating)
        session.commit()
        print(f"{new_rating} added to database.")

    def __repr__(self):
        return (
            f"\nRating\n"
            + f"id = {self.id}\n"
            + f"user_id = {self.user_id}\n"
            + f"user_name = {self.user.name}\n"
            + f"coffee_id = {self.coffee_id}\n"
            + f"coffee_roaster = {self.coffee.roaster}\n"
            + f"coffee_name = {self.coffee.name}\n"
            + f"rating = {self.rating}\n"
        )
