
def base_graphic(team_name):
    if team_name.base_list[0] == False and team_name.base_list[1] == False and team_name.base_list[2] == False:
        print("  2  ")
        print("3   1")
        print("  * ")
    elif team_name.base_list[0] == True and team_name.base_list[1] == False and team_name.base_list[2] == False:
        print("  2  ")
        print("3   @")
        print("  * ")
    elif team_name.base_list[0] == True and team_name.base_list[1] == True and team_name.base_list[2] == False:
        print("  @  ")
        print("3   @")
        print("  * ")
    elif team_name.base_list[0] == True and team_name.base_list[1] == True and team_name.base_list[2] == True:
        print("  @  ")
        print("@   @")
        print("  * ")
    elif team_name.base_list[0] == False and team_name.base_list[1] == True and team_name.base_list[2] == True:
        print("  @  ")
        print("@   1")
        print("  * ")
    elif team_name.base_list[0] == True and team_name.base_list[1] == False and team_name.base_list[2] == True:
        print("  2  ")
        print("@   @")
        print("  * ")
    elif team_name.base_list[0] == False and team_name.base_list[1] == True and team_name.base_list[2] == False:
        print("  @  ")
        print("3   1")
        print("  * ")
    else:
        print("  2  ")
        print("@   1")
        print("  * ")


def scorebug(batting_team_name, other_team_name):
    print()
    base_graphic(batting_team_name)
    print()
    if batting_team_name.home_team == False:
        print(f"Top {batting_team_name.inning}, {batting_team_name.outs} out")
    else:
        print(
            f"Bottom {batting_team_name.inning}, {batting_team_name.outs} out")
    print()
    if batting_team_name.home_team == False:
        print(f"{batting_team_name.name}: {batting_team_name.runs}\n{other_team_name.name}: {other_team_name.runs}")
    else:
        print(f"{other_team_name.name}: {other_team_name.runs}\n{batting_team_name.name}: {batting_team_name.runs}")
    print()
