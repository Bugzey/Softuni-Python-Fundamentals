#   Match valid full names
import re

name_pattern = re.compile(r'\b[A-Z][a-z]+\b \b[A-Z][a-z]+\b')
user_input = input()

match = re.finditer(name_pattern, user_input)
result = [item.group() for item in match]

print(*result, sep = ' ')

