import random
import score
from batting import AtBat
from team import Team

team1 = input("Player 1, choose a team name: ")
team2 = input("Player 2, choose a team name: ")


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
