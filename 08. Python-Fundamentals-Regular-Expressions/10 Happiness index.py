#   Count and data mine smileys
import re
def lazybones(name, str):
    str = str.split(', ')
    result = '|'.join([re.escape(item) for item in str])
    result = f'(?P<{name}>' + result + ')'
    return(result)

str_happy = ':), :D, ;), :*, :], ;], :}, ;}, (:, *:, c:, [:, [;'
str_sad = ':(, D:, ;(, :[, ;[, :{, ;{, ):, :c, ]:, ];'
pattern_happy = lazybones('happy', str_happy)
pattern_sad = lazybones('sad', str_sad)

user_input = input()

match_happy = re.finditer(pattern_happy, user_input)
match_sad = re.finditer(pattern_sad, user_input)

nr_happy = 0
nr_sad = 0

for match in match_happy:
    nr_happy += 1

for match in match_sad:
    nr_sad += 1

happiness_index = nr_happy / nr_sad

icon = ':D' if happiness_index >= 2 else ':)' if happiness_index > 1 else ':|' if happiness_index == 1 else ':('

line1 = f'Happiness index: {happiness_index:.2f} {icon}'
line2 = f'[Happy count: {nr_happy}, Sad count: {nr_sad}]'
print(line1, line2, sep = '\n')
