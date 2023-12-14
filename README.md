# Python Baseball Game
This is a Python-based two player baseball game that can be played in 
the terminal using a command-line interface.

## Usage
```bash
python baseball.py
```

Gameplay is pretty straightforward: each player will be prompted
to create a team name, then to either swing or take a pitch when their 
team is up to bat, and the result will be communicated by the game. 
There is also a graphic to track the score, inning, number of
outs, and current baserunners, if any. [Click here](https://asciinema.org/a/sbFJ7I2jqIE7gX4K2onOcLHl7) to watch
a video of a sample inning being played.

## API Reference Table
| Endpoint    | Description |
| ----------- | ----------- |
| GET base_url/players      | Fetches all players       |
| GET base_url/players/id      | Fetches specified player       |
| POST base_url/players      | Adds new player (req'd fields: team_id, name, primary_position, average, rbi, homers)       |
| PUT base_url/players/id      | Updates specified player's stats/info       |
| DELETE base_url/players/id      | Deletes specified player       |
| GET base_url/teams      | Fetches all teams       |
| GET base_url/teams/id   | Fetches specified team        |

## Questions
### 1. How did the project's design evolve over time?
I built the core of the game in the Python fundamentals course to practice OOP principles. Once we started this course, I realized that I could further develop it to create a three-tiered architecture for it. I have been focusing on developing a database of information about Major League Baseball teams and players, choosing appropriate attributes, and designing the relationship between the entities. I've also been exploring MLB's StatsAPI website, which has exposed endpoints but no public documentation--so I've had to dig for everything!
### 2. Did you choose an ORM or raw SQL? Why?
I chose to utilize the SQLAlchemy ORM, mainly because the queries required for this game are simple and straightforward, but also because I have been learning to write Python scripts to parse JSON files I've found on the MLB StatsAPI website. I was able to combine those two steps into one file that I created from scratch (with a little help from ChatGPT), which taught me some valuable things about SQLAlchemy, JSON, and Python, and how they all interact and can be utilized in tandem. This has been a fun process and I've already learned alot, though I have a good ways to go to fully build out the project the way I want to (see below for more information about that).
### 3. What future improvements are in store, if any?
On the data layer, I would like to first find all the data I need from StatsAPI and write Python scripts to parse those JSON files for the specific player data that I need, subsequently using SQLAlchemy to feed this data into my database. Once I have accomplished that, I would like to automate the process of updating player stats over the course of the baseball season at regular time intervals (perhaps once a week). I think a better understanding of Flask might help with this as well. Finally, after this bootcamp concludes I would like to build a basic GUI to have a more sophisticated presentation layer than just the CLI. With all of those pieces fully fleshed out, I'll have a project that demonstrates a solid three-tiered architecture, and I can use those skills to develop new projects in the future.