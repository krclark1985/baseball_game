import json
from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres@localhost:5432/baseball_data', echo=True)

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

# Load JSON file as Python object
with open('teams.json') as teams:
    teams_data = json.load(teams)

# Iterate through teams_data object, searching for MLB teams
# in the list and adding them teams database when found
teams_dict = {}
i = 0
while True:
    try: 
        if teams_data['teams'][i]['sport']['id'] == 1:
            new_team = Team(name = teams_data['teams'][i]['name'], mlb_id = teams_data['teams'][i]['id'])
            session.add(new_team)
            i += 1
        else:
            i += 1
    except:
        break

session.commit()
