#   Read every odd file and write it out
in_file = open('Resources/01. Odd Lines/Input.txt', 'r').read()
result = in_file.split('\n')
print(*result[1::2], sep = '\n')
