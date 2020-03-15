#   Insert line numbers
in_file = open('Resources/02. Line Numbers/Input.txt', 'r').read().split('\n')
result = [str(number + 1) + '. ' + item for number, item in enumerate(in_file)][:-1]
print(*result, sep = '\n')

out_str = '\n'.join(result)

open('output/02.txt', 'w').write(out_str)

