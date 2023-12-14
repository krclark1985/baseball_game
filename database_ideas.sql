CREATE TABLE teams (
    id SERIAL PRIMARY KEY,
    city TEXT NOT NULL,
    team_name TEXT NOT NULL UNIQUE
)

-- consider splitting name attribute into first and last?
-- look into giving non-nullable offensive stats a default
-- value for pitchers (otherwise I'll need to give them zeroes
-- when inserting pitchers into lineup; could also just leave
-- pitchers out of the game...)
CREATE TABLE players (
    id SERIAL PRIMARY KEY,
    team_id INT,
    name TEXT NOT NULL UNIQUE,
    lineup_position INT UNIQUE,
    primary_position CHAR(2) NOT NULL,
    average NUMERIC NOT NULL,
    rbi INT NOT NULL,
    homers INT NOT NULL,
    obp NUMERIC NOT NULL,
    slugging NUMERIC NOT NULL,
    ops NUMERIC NOT NULL
)

-- Creates foreign key constraint to specify relationship
-- between players table and teams table (i.e. each player
-- on a team will be assigned a team_id to match them to
-- their team)
ALTER TABLE players
ADD CONSTRAINT fk_players_teams
FOREIGN KEY (team_id)
REFERENCES teams;