#SQLAlchemy is being used to access the PostgreSQL database

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base, sessionmaker
from decouple import config


url = URL.create(                    #creates the URL object which is used as the argument for the create_engine function
    drivername="postgresql",
    username=config("DB_USER"),
    password=config("DB_PASSWORD"),
    host="localhost",
    database="mydb",
    port=5432
)

engine = create_engine(url)         #creates an engine object that manages connections to the database using a URL that contains the connection information for the database
SessionLocal = sessionmaker(bind=engine)     #factory for creating Session objects that are used to interact with the database
Base = declarative_base()            #factory function that returns a base class that can be subclassed to define mapped classes for the ORM

class Conversation(Base):               
    __tablename__ = "conversations"   #mapped class that inherits from Base and maps to the conversation table

    id = Column(Integer, primary_key=True, index=True)
    sender = Column(String)
    message = Column(String)
    response = Column(String)


Base.metadata.create_all(engine)     # creates all tables in the database if they do not exist