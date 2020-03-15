#   Parse valid crypic messages
#   A command is valid when the input starts with digits, 
#   continues to alphabetic characters and ends in any 
#   characters but alphabetical.

import re
pattern = re.compile(r'(?P<left>\d+)(?P<command>[A-Za-z]+)(?P<right>[^A-Za-z]*)$')

while True:
    user_input = input()
    if user_input == 'Over!':
        break
    verif_number = int(input())

    match = re.match(pattern, user_input)

    if match is None:
        continue

    message = match.group('command')
    left = match.group('left')
    right = match.group('right')
    right = filter(str.isdigit, right)

    if len(message) != verif_number:
        continue

    code_left = [message[int(index)] if int(index) < len(message) else ' ' for index in list(left)]
    code_right = [message[int(index)] if int(index) < len(message) else ' ' for index in list(right)]

    code_joined = ''.join(code_left + code_right)
    
    result = f'{message} == {code_joined}'
    print(result)
