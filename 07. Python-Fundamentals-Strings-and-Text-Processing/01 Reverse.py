#   Reverse an input string
user_input = input()
input_length = len(user_input)
result = reversed(user_input)
print(*result, sep = '')
