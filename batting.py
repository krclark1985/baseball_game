import random
import score


class AtBat:
    def __init__(self, batting_team_name, other_team_name):
        self.batting_team_name = batting_team_name
        self.other_team_name = other_team_name
        self.strike_counter = 0
        self.ball_counter = 0

    def out_checker(self, batting_team_name):
        if self.strike_counter == 3:
            print("You're out!")
            self.batting_team_name.outs += 1
            self.strike_counter = 0
            self.ball_counter = 0
            score.scorebug(self.batting_team_name, self.other_team_name)
        elif self.ball_counter == 4:
            print("Batter walks")
            self.strike_counter = 0
            self.ball_counter = 0
            self.batting_team_name.runner_func(1)
            score.scorebug(self.batting_team_name, self.other_team_name)
        if self.batting_team_name.outs == 3:
            self.batting_team_name.reset()

    def at_bat_func(self):
        pitch = random.randint(1, 8)
        while True:
            choice = input("Input 1 to swing or 2 to take the pitch: ")
            if choice.isnumeric() and int(choice) >= 1 and int(choice) <= 2:
                choice = int(choice)
                break
            else:
                print("Invalid input")
        if pitch <= 5 and choice == 2:
            self.strike_counter += 1
            print("Called strike.")
            print(f"{self.ball_counter}-{self.strike_counter} count")
        elif pitch <= 5 and choice == 1:
            self.hit_func()
            score.scorebug(self.batting_team_name, self.other_team_name)
        elif pitch >= 6 and choice == 1:
            self.strike_counter += 1
            print("Swing and a miss!")
            print(f"{self.ball_counter}-{self.strike_counter} count")
        else:
            self.ball_counter += 1
            print("Ball")
            print(f"{self.ball_counter}-{self.strike_counter} count")
        self.out_checker(self.batting_team_name)

    def hit_func(self):
        outcome = random.randint(1, 100)
        if outcome < 20:
            # Make this about 19%
            print("Batter hits a single.")
            self.batting_team_name.runner_func(1)
            self.strike_counter = 0
            self.ball_counter = 0
        elif outcome < 44:
            # Make this 24%
            print("Foul ball.")
            if self.strike_counter < 2:
                self.strike_counter += 1
            print(f"{self.ball_counter}-{self.strike_counter} count")
        elif outcome < 55:
            # MLB average is about 11%
            print("Swing and a miss!")
            self.strike_counter += 1
            print(f"{self.ball_counter}-{self.strike_counter} count")
        elif outcome < 68:
            # Make this 13%
            print("Groundout.")
            self.batting_team_name.outs += 1
            if self.batting_team_name.outs < 3:
                self.batting_team_name.move_runners(1)
                self.batting_team_name.base_check()
                self.strike_counter = 0
                self.ball_counter = 0
        elif outcome < 80:
            # Make this 12%
            print("Flyout.")
            self.batting_team_name.outs += 1
            self.strike_counter = 0
            self.ball_counter = 0
        elif outcome < 90:
            # Make this about 10% of the time
            print("Batter hits a double!")
            self.batting_team_name.runner_func(2)
            self.strike_counter = 0
            self.ball_counter = 0
        elif outcome < 93:
            # Make this about 3% of the time
            print("Batter hits a triple!")
            self.batting_team_name.runner_func(3)
            self.strike_counter = 0
            self.ball_counter = 0
        else:
            # Make this about 8% of the time
            print("Batter hits a home run!!!")
            self.batting_team_name.runner_func(4)
            self.strike_counter = 0
            self.ball_counter = 0
