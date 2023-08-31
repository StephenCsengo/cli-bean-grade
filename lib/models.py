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
        print(f"New coffee {coffee.roaster} {coffee.name} added.")

    @classmethod
    def find_by_id(cls, coffee_id):
        coffee_id_search = session.query(cls).filter(cls.id.like(coffee_id)).first()
        return coffee_id_search

    @classmethod
    def delete_by_id(cls, coffee_id):
        Rating.delete_by_coffee_id(coffee_id=coffee_id)
        coffee_removal = session.query(cls).filter(cls.id == coffee_id).delete()
        session.commit()

    @classmethod
    def update_roaster(cls, id, new_roaster):
        session.query(cls).filter(cls.id == id).update({cls.roaster: new_roaster})
        session.commit()

    @classmethod
    def update_name(cls, id, new_name):
        session.query(cls).filter(cls.id == id).update({cls.roaster: new_name})
        session.commit()

    @classmethod
    def update_roast_level(cls, id, new_roast_level):
        session.query(cls).filter(cls.id == id).update({cls.roaster: new_roast_level})
        session.commit()

    @classmethod
    def get_all_coffees(cls):
        coffees = session.query(Coffee).all()
        return coffees

    @classmethod
    def get_recent_coffee(cls):
        coffee = session.query(Coffee).order_by(Coffee.id.desc()).first()
        return coffee

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
    def add_new_rating(cls, user_id, coffee_id, rating):
        new_rating = cls(user_id=user_id, coffee_id=coffee_id, rating=rating)
        session.add(new_rating)
        session.commit()
        print(
            f"Rating of {new_rating.rating} by {new_rating.user.name} for {new_rating.coffee.roaster} {new_rating.coffee.name} added to database."
        )

    @classmethod
    def update_rating(cls, id, new_rating):
        session.query(cls).filter(cls.id == id).update({cls.rating: new_rating})
        session.commit()

    @classmethod
    def delete_by_coffee_id(cls, coffee_id):
        rating_removal = session.query(cls).filter(cls.coffee_id == coffee_id).all()
        for rating in rating_removal:
            session.delete(rating)
            session.commit()

    @classmethod
    def delete_by_rating_id(cls, id):
        rating_removal = session.query(cls).filter(cls.id == id).first()
        session.delete(rating_removal)
        session.commit()

    @classmethod
    def delete_by_user_id(cls, user_id):
        rating_removal = Rating.get_all_ratings(user_id=user_id)
        for rating in rating_removal:
            session.delete(rating)
            session.commit()

    @classmethod
    def get_all_ratings(cls, user_id):
        ratings = session.query(cls).filter(cls.user_id == user_id).all()
        return ratings

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
