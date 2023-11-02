
class Team:
    def __init__(self, name, home_team):
        self.name = name
        self.home_team = home_team
        self.runs = 0
        self.inning = 1
        self.outs = 0
        self.num_runners = 0
        self.runner_index = 0
        self.runner_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.base_list = [False, False, False]

    def run_func(self, runs_to_add):
        self.runs += runs_to_add

    def runner_func(self, num_bases):
        self.base_reset()
        self.new_runner(num_bases)
        self.move_runners(num_bases)
        self.base_check()

    def new_runner(self, num_bases):
        if num_bases == 4:
            self.run_func(1)
        else:
            self.runner_list[self.runner_index] = num_bases
            self.num_runners += 1
            if self.runner_index == 8:
                self.runner_index = 0
            else:
                self.runner_index += 1

    def move_runners(self, num_bases):
        if self.num_runners >= 1:
            if num_bases == 4:
                for i in range(0, self.runner_index + 1, 1):
                    if self.runner_list[i] > 0:
                        self.runner_list[i] = 0
                        self.run_func(1)
            else:
                for i in range(0, self.runner_index - 1, 1):
                    if self.runner_list[i] > 0:
                        self.runner_list[i] += num_bases
                        if self.runner_list[i] >= 4:
                            self.run_func(1)
                            self.runner_list[i] = 0

    def base_check(self):
        for i in range(len(self.runner_list)):
            if self.runner_list[i] == 1:
                self.base_list[0] = True
            elif self.runner_list[i] == 2:
                self.base_list[1] = True
            elif self.runner_list[i] == 3:
                self.base_list[2] = True

    def base_reset(self):
        self.base_list = [False, False, False]

    def reset(self):
        self.num_runners = 0
        self.runner_index = 0
        self.runner_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.base_list = [False, False, False]
        self.inning += 1
        # if self.inning == 10, compare score, print "Game Over, ___ team wins {score}!"
