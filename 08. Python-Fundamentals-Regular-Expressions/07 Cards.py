#   Get playing cards
import re
pattern = re.compile(r'((10|[2-9])|[JKQA])([SHDC])')
result = []

user_input = input()
match_iter = re.finditer(pattern, user_input)

for match in match_iter:
    result.append(match.group())

print(*result, sep = ' ')
