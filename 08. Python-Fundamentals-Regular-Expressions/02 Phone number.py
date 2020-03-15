#   Match valid Bulgarian phone numbers
import re
pattern = re.compile(r'\+359([ -])2\1\d{3}\1\d{4}\b')

user_input = input()
match = re.finditer(pattern, user_input)
result = [match.group() for match in match]

print(*result, sep = ' ')
