#   Regex filtering
import re

key_pattern = re.compile(r'[starSTAR]')
#info_pattern = re.compile(r'.*@(?P<planet>[a-zA-Z]+).*:(?P<pop>\d+).*\!(?P<command>[AD])\!.*\-\>(?P<soldier>\d+)')
info_pattern = re.compile(r'.*@(?P<planet>[a-zA-Z]+)[^@\-\!\:]*:(?P<pop>\d+)[^@\-\!\:]*\!(?P<command>[AD])\![^@\-\!\:]*\-\>(?P<soldier>\d+)')
attacked = []
destroyed = []

n_lines = int(input())
user_input = [input() for item in range(n_lines)]

for line in user_input:
    key = len(re.findall(key_pattern, line))
    message = ''.join([chr(ord(letter) - key) for letter in line])
    match = re.match(info_pattern, message)

    if match is not None:
        planet, pop, attack, soldier = match.group('planet'), match.group('pop'), match.group('command'), match.group('soldier')
        if attack == 'A':
            attacked.append(planet)
        elif attack == 'D':
            destroyed.append(planet)

nr_attacked = len(attacked)
nr_destroyed = len(destroyed)

attacked.sort(key = str.lower)
destroyed.sort(key = str.lower)

attacked = [f'-> {item}' for item in attacked]
destroyed = [f'-> {item}' for item in destroyed]

print(f'Attacked planets: {nr_attacked}')
if len(attacked) > 0:
    print(*attacked, sep = '\n')

print(f'Destroyed planets: {nr_destroyed}')
if len(destroyed) > 0:
    print(*destroyed, sep = '\n')
