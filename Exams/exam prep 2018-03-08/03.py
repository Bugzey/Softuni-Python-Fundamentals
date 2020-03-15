#   Use regex to clean football results, custom pattern
import re

class Team:
    def __init__(self, name):
        self.name = name
        self.points, self.goals, self.matches = 0, 0, 0

    def win(self, goals):
        self.points += 3
        self.goals += goals

    def loss(self, goals):
        self.points += 0
        self.goals += goals

    def draw(self, goals):
        self.points += 1
        self.goals += goals

    def __gt__(self, other):
        if type(other) is not Team:
            raise ValueError('Comparison only possible between teams.')

        gt = self.points > other.points or (self.points == other.points and self.name < other.name)
        return(gt)

    def __eq__(self, other):
        if type(other) is not Team:
            raise ValueError('Comparison only possible between teams.')

        eq = self.points == other.points and self.name == other.name
        return(eq)

    def __str__(self):
        return(self.name)

class League:
    def __init__(self):
        self.teams = {}

    def match(self, team1, team2, score1, score2):
        for team in [team1, team2]:
            if team not in self.teams.keys():
                self.teams[team] = Team(team)

        if score1 > score2:
            self.teams[team1].win(score1)
            self.teams[team2].loss(score2)
        elif score1 < score2:
            self.teams[team1].loss(score1)
            self.teams[team2].win(score2)
        else:
            self.teams[team1].draw(score1)
            self.teams[team2].draw(score2)

    def __str__(self):
        teams = self.teams.values()
        standings = enumerate(sorted(teams, reverse = True))
        goals = [(team.goals, team.name) for team in teams]
        goal_standings = sorted(goals, key = lambda x: (-x[0], x[1]), reverse = False)
        line1 = 'League standings:'
        line2 = '\n'.join([f'{str(nr + 1)}. {team.name} {str(team.points)}' for nr, team in standings])
        line3 = 'Top 3 scored goals:'
        line4 = '\n'.join([f'- {team} -> {goals}' for goals, team in goal_standings][0:3])
        result = '\n'.join([line1, line2, line3, line4])

        return(result)

league = League()
user_key = re.escape(input())
pattern = re.compile(rf'.*?({user_key})(?P<team1>\w+)\1.*?\1(?P<team2>\w+)\1.*?(?P<score1>\d+):(?P<score2>\d+)$')

while True:
    line = input()
    if line == 'final':
        break

    match = re.match(pattern, line)
    if match is None:
        continue

    team1 = match.group('team1')
    team2 = match.group('team2')
    score1 = match.group('score1')
    score2 = match.group('score2')

    team1 = team1.upper()[-1::-1]
    team2 = team2.upper()[-1::-1]
    score1 = int(score1)
    score2 = int(score2)

    league.match(team1, team2, score1, score2)

print(league)
