from sqlalchemy import create_engine, Column, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

engine = create_engine("sqlite:///data/aura_memory.db")
Session = sessionmaker(bind=engine)
Base = declarative_base()

class UserMemory(Base):
    __tablename__ = "user_memory"
    name = Column(String, primary_key=True)
    last_sentiment = Column(String)

class Interaction(Base):
    __tablename__ = "interactions"
    id = Column(String, primary_key=True)
    name = Column(String)
    sentiment = Column(String)
    timestamp = Column(DateTime)

Base.metadata.create_all(engine)

def save_user(name, sentiment):
    session = Session()

    user = session.get(UserMemory, name)
    if user:
        user.last_sentiment = sentiment
    else:
        user = UserMemory(name=name, last_sentiment=sentiment)
        session.add(user)

    interaction = Interaction(
        id=str(datetime.now().timestamp()),
        name=name,
        sentiment=sentiment,
        timestamp=datetime.now()
    )
    session.add(interaction)

    session.commit()
    session.close()

def get_all_interactions():
    session = Session()
    data = session.query(Interaction).all()
    session.close()
    return data
