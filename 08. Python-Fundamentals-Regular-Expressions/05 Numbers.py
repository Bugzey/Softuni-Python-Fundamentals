#   Match numbers
import re
pattern = re.compile(r'(^|(?<=\s))-?\d+(\.\d+)*($|(?=\s))')
user_input = input()

match = re.finditer(pattern, user_input)
result = [item.group() for item in match]
print(*result, sep = " ")
