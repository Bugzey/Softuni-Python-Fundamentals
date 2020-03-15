#   Match dates with matching separators
import re
pattern = re.compile(r'(?P<day>\d{2})(?P<sep>[-./])(?P<month>[A-Z][a-z]{2})\2(?P<year>\d{4})')

user_input = input()
match = re.finditer(pattern, user_input)
result = [f'Day: {item.group("day")}, Month: {item.group("month")}, Year: {item.group("year")}' for item in match]

print(*result, sep = '\n')
