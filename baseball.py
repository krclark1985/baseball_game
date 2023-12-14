import random
import score
from batting import AtBat
from team import Team

team1 = input("Player 1, choose a team name: ")
team2 = input("Player 2, choose a team name: ")


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

'''
p1_team = Team(team1, True)
p2_team = Team(team2, False)

while p1_team.inning < 10 and p2_team.inning < 10:
    up_to_bat = AtBat(p2_team, p1_team)
    print(f"\n{p2_team.name} are up! Player 2 is now playing.\n")
    while p2_team.outs < 3:
        up_to_bat.at_bat_func()
    p2_team.outs = 0
    print(f"\n3 outs! End of inning. {p1_team.name} are up next.\n")

    up_to_bat = AtBat(p1_team, p2_team)
    print(f"\n{p1_team.name} are up! Player 1 is now playing.\n")
    while p1_team.outs < 3:
        up_to_bat.at_bat_func()
    p1_team.outs = 0
    print(f"\n3 outs! End of inning. {p2_team.name} are up next.\n")
if p1_team.runs > p2_team.runs:
    print(
        f"\nFINAL SCORE\n{p2_team.name}: {p2_team.runs}\n{p1_team.name}: {p1_team.runs}\n")
    print(f"{p1_team.name} win! Congrats Player 1!")
elif p2_team.runs > p1_team.runs:
    print(
        f"\nFINAL SCORE\n{p2_team.name}: {p2_team.runs}\n{p1_team.name}: {p1_team.runs}\n")
    print(f"{p2_team.name} win! Congrats Player 2!")
else:
    # Make a conditional for when the game is still tied after 9 innings
    print("It's a tie ballgame.")
'''
