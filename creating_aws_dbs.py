from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://krclark1985:R!j78dY1@baseball-data.cdgwe6ke4hk2.us-west-1.rds.amazonaws.com:5432/baseball-data', echo=True)

# Define a base class for declarative class definitions
Base = declarative_base()

# Define a simple model for Team class
class Team(Base):
    __tablename__ = 'teams'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(50), nullable=False)
    mlb_id = Column(Integer, nullable=False)

# Create the table
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

session.commit()
