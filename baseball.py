import random
import score
from batting import AtBat
from team import Team

teams_list = ['Padres', 'Dodgers', 'Diamondbacks']

def print_teams(teams):
    i = 1
    print("MLB TEAMS:")
    for t in teams:
        print(f"{i} - {t}")
        i += 1

print_teams(teams_list)
while True:
    team1_choice = input("Player 1, enter number of team choice: ")
    if team1_choice.isnumeric() == False:
        team1_choice = input("Player 1, enter number of team choice: ")
    elif int(team1_choice) > len(teams_list):
        team1_choice = input("Player 1, enter number of team choice: ")
    elif int(team1_choice) == 0:
        team1_choice = input("Player 1, enter number of team choice: ")
    else:
        team1_choice = int(team1_choice)
        break
team1 = teams_list[team1_choice - 1]
del teams_list[team1_choice - 1]
print_teams(teams_list)
while True:
    team2_choice = input("Player 2, enter number of team choice: ")
    if team2_choice.isnumeric() == False:
        team2_choice = input("Player 2, enter number of team choice: ")
    elif int(team2_choice) > len(teams_list):
        team2_choice = input("Player 2, enter number of team choice: ")
    elif int(team2_choice) == 0:
        team2_choice = input("Player 2, enter number of team choice: ")
    else:
        team2_choice = int(team2_choice)
        break
team2 = teams_list[team2_choice - 1]

print(f"\n{team1} (Player 1) \n\nvs.\n\n{team2} (Player 2)\n")

class Game:
    def __init__(self, team_class, home_team_name, home_bool, away_team_name, away_bool):

        self.home_team = team_class(home_team_name, home_bool)
        self.away_team = team_class(away_team_name, away_bool)

    def play(self):
        while self.home_team.inning < 10 and self.away_team.inning < 10:
            up_to_bat = AtBat(self.away_team, self.home_team)
            print(f"\n{self.away_team.name} are up! Player 2 is now playing.\n")
            while self.away_team.outs < 3:
                up_to_bat.at_bat_func()
            self.away_team.outs = 0
            print(
                f"\n3 outs! End of inning. {self.home_team.name} are up next.\n")

            up_to_bat = AtBat(self.home_team, self.away_team)
            print(f"\n{self.home_team.name} are up! Player 1 is now playing.\n")
            while self.home_team.outs < 3:
                up_to_bat.at_bat_func()
            self.home_team.outs = 0
            print(
                f"\n3 outs! End of inning. {self.away_team.name} are up next.\n")
        if self.home_team.runs > self.away_team.runs:
            print(
                f"\nFINAL SCORE\n{self.away_team.name}: {self.away_team.runs}\n{self.home_team.name}: {self.home_team.runs}\n")
            print(f"{self.home_team.name} win! Congrats Player 1!\n")
        elif self.away_team.runs > self.home_team.runs:
            print(
                f"\nFINAL SCORE\n{self.away_team.name}: {self.away_team.runs}\n{self.home_team.name}: {self.home_team.runs}\n")
            print(f"{self.away_team.name} win! Congrats Player 2!\n")
        else:
            # Make a conditional for when the game is still tied after 9 innings
            print("It's a tie ballgame.")


new_game = Game(Team, team1, True, team2, False)
new_game.play()


