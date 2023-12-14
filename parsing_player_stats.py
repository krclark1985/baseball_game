import requests

# Figure out how to automate this for an entire roster (minus pitchers maybe?)
# by first iterating through the roster to make a list of mlb player ids, then
# looping through that and running the code below (probably best to make it one
# big function); NEXT STEP AFTER THAT: How to post to Postgres database?

# Look up Python cronjob for automatic updates (weekly for baseball_data db?)

team_player_ids = []
team_player_dicts = []

def get_team_players(team_mlb_id):
    url = f'https://statsapi.mlb.com/api/v1/teams/{team_mlb_id}/roster'
    team_roster = requests.get(url)
    team_roster = team_roster.json()

    i = 0
    while True:
        try:
            if team_roster["roster"][i]["position"]["abbreviation"] != "P":
                team_player_ids.append(team_roster["roster"][i]["person"]["id"])
                i += 1
            else:
                i += 1
        except:
            break       


# Need to either make a dictionary or link to database to link player
# to team in db via mlb_id, so I don't have to input team_id by hand
def get_player_stats(player_id):

    url1 = f'https://statsapi.mlb.com/api/v1/people/{player_id}'
    player_info = requests.get(url1)
    player_info = player_info.json()

    player_dict = {
        'team_id': 18, 'name': player_info['people'][0]['fullName'],
        'primary_position': player_info['people'][0]['primaryPosition']['abbreviation']
    }

    url2 = f'https://statsapi.mlb.com/api/v1/people/{player_id}/stats?season=2023&group=hitting&stats=season'
    player_stats = requests.get(url2)
    player_stats = player_stats.json()

    player_dict.update({'average': player_stats['stats'][0]['splits'][0]['stat']['avg'],
                    'rbi': player_stats['stats'][0]['splits'][0]['stat']['rbi'], 
                    'homers': player_stats['stats'][0]['splits'][0]['stat']['homeRuns'],})
    
    team_player_dicts.append(player_dict)

get_team_players(135)

n = 0
while n < len(team_player_ids):
    get_player_stats(team_player_ids[n])
    n += 1

for dict in team_player_dicts:
    print(dict)


# player_json = json.dumps(player_dict)
# print(player_json)
# requests.post('http://localhost:5000/players', json=player_json)

