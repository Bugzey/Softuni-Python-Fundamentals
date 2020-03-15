#   Match hexadecimal digits (0x) optional
import re
pattern = re.compile(r'\b(0x)*[A-F0-9]+\b')

user_input = input()
match = re.finditer(pattern, user_input)
result = [item.group() for item in match]

print(*result, sep = ' ')
