from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import User, Coffee, Rating

if __name__ == "__main__":
    print("Seeding database...")
    engine = create_engine("sqlite:///db/beangrade.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(User).delete()
    session.commit()

    users = [User(name="Stephen"), User(name="Kristin"), User(name="Test User")]
    session.add_all(users)
    session.commit()

    session.query(Coffee).delete()
    session.commit()

    coffees = [
        Coffee(roaster="Verve", name="Larrea Blend", roast_level="Medium"),
        Coffee(roaster="Methodical", name="Blue Boy", roast_level="Medium"),
        Coffee(roaster="Atomic", name="Space Cadet", roast_level="Light"),
        Coffee(roaster="Irving Farm", name="Gotham", roast_level="Dark"),
        Coffee(roaster="Perkatory", name="Costa Rica Esperanza", roast_level="Medium"),
    ]
    session.add_all(coffees)
    session.commit()

    session.query(Rating).delete()
    session.commit()

    ratings = [
        Rating(user_id=1, coffee_id=4, rating=2),
        Rating(user_id=2, coffee_id=2, rating=10),
        Rating(user_id=2, coffee_id=5, rating=8),
        Rating(user_id=3, coffee_id=2, rating=2),
        Rating(user_id=1, coffee_id=1, rating=9),
        Rating(user_id=1, coffee_id=3, rating=6),
    ]
    session.add_all(ratings)
    session.commit()

    print("Seeding complete!")
