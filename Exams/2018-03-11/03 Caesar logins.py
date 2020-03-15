#   Crack an uncrackable cypher
import re
pattern = re.compile(r'^([\/\\]{1})[^a-zA-Z0-9]*(?P<username>[a-zA-Z0-9]+)[^a-zA-Z0-9]*(?P=username)[^a-zA-Z0-9]*(?P<password>[a-zA-Z0-9]+)[^a-zA-Z0-9]*(?P=password)[^a-zA-Z0-9]*(?P=username)[^a-zA-Z0-9]*(?P=password)[^a-zA-Z0-9]*\1$')

while True:
    user_input = input()

    if user_input == '/end/':
        break

    match = re.match(pattern, user_input)

    if match is None:
        continue

    user, password = match.group('username'), match.group('password')

    cleaned_input = user_input.replace(user, '')
    cleaned_input = cleaned_input.replace(password, '')
    cleaned_input = cleaned_input[1:-1]

    key = len(cleaned_input)

    user = ''.join([chr(ord(letter) - key) for letter in user])
    password = ''.join([chr(ord(letter) - key) for letter in password])

    result = f'user: {user}, pass: {password}'
    print(result)
