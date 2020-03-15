#   Reverse of serialising, receive letter: index1/index2..., print the string
str_dict = {}
max_index = 0

while True:
    user_input = input().split(':')
    if user_input[0] == 'end':
        break

    letter, indices = user_input
    indices = list(map(int, indices.split('/')))

    if letter not in str_dict.keys():
        str_dict[letter] = indices
    else:
        str_dict[letter].append(indices)

    max_index = max(str_dict[letter]) if max(str_dict[letter]) > max_index else max_index
    #print(max(str_dict[letter]))

result = ['' for item in range(max_index + 1)]

for key in str_dict.keys():
    for index in str_dict[key]:
        result[index] = key

print(''.join(result))
