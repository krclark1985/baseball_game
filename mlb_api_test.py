import json

with open('teams.json') as teams:
    teams_data = json.load(teams)

teams_dict = {}
i = 0
while True:
    try: 
        if teams_data['teams'][i]['sport']['id'] == 1:
            # print(teams_data['teams'][i]['name'], ':', teams_data['teams'][i]['id'])
            teams_dict.update({teams_data['teams'][i]['name']: teams_data['teams'][i]['id']})
            i += 1
        else:
            i += 1
    except:
        break
    
    
