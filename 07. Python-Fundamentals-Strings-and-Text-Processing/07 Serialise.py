#   Get a string, print a list of chars and the indices of those chars
user_input = input()
str_order = list(user_input)
str_dict = {}

str_dict = {key: [] for key in str_order}
for key in str_dict.keys():
    start_index = 0
    while True:
        try:
            start_index = user_input.index(key, start_index)
            str_dict[key].append(str(start_index))
            start_index += 1
        except ValueError:
            break

result = [key + ':' + '/'.join(str_dict[key]) for key in str_dict.keys()]
print(*result, sep = '\n')
