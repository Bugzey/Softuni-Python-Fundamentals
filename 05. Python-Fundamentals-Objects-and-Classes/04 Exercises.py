#   Make a course exercise document generator via a class
class Exercise:
    def __init__(self, topic, course_name, judge_contest_link, problems):
        self.topic = topic
        self.course_name = course_name
        self.judge_contest_link = judge_contest_link
        self.problems = problems.split(', ')

    #def __str__(self):
    def print(self):
        print('Exercises: ' + self.topic)
        print("Problems for exercises and homework for the \"" + self.course_name + "\" course @ SoftUni.")
        print('Check your solutions here: ' + self.judge_contest_link)
        print(*[str(index + 1) + '. ' + self.problems[index] for index in list(range(len(self.problems)))], sep = "\n")
        

user_input = ""
exercise_list = []

while True:
    user_input = input().split(" -> ")
    if user_input[0] == "go go go":
        break

    cur_info = user_input[:-1]
    cur_exercises = user_input[-1]

    cur_exercise = Exercise(*cur_info, cur_exercises)
    exercise_list.append(cur_exercise)

[exercise.print() for exercise in exercise_list]

