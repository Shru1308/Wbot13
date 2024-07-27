#SQLAlchemy sed to access the PostgreSQL database
#db created to store the conversations

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base, sessionmaker
from decouple import config


url = URL.create(                    # creates the URL object
    drivername="postgresql",         
    username=config("DB_USER"),
    password=config("DB_PASSWORD"),
    host="localhost",
    database="mydb",
    port=5432
)


engine = create_engine(url)         # creates an engine object, connecting to db using the url
SessionLocal = sessionmaker(bind=engine)     # factory for creating Session objects used to interact with the database
Base = declarative_base()            # factory function returning base class, can be subclassed to define mapped classes


class Conversation(Base):               
    __tablename__ = "conversations"   # mapped class that inherits from Base and maps to the conversation table

    id = Column(Integer, primary_key=True, index=True)
    sender = Column(String)
    message = Column(String)
    response = Column(String)


Base.metadata.create_all(engine)     # creating tables in db if not exist
