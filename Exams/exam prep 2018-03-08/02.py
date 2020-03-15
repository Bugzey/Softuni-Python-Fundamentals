#   String commander v02
def exchange(input_list, length):
    result = input_list[(length + 1):] + input_list[:(length + 1)]
    return(result)

def extreme(input_list, extreme_type, num_type):
    if extreme_type == 'max':
        func = max
    elif extreme_type == 'min':
        func = min

    cur_mod = 0 if num_type == 'even' else 1 if num_type == 'odd' else -1
    all_num_types = list(filter(lambda y: y % 2 == cur_mod, input_list))
    if len(all_num_types) == 0:
        return('No matches')

    cur_extreme = func(all_num_types)

    indices = [index for index, num in enumerate(input_list) if num == cur_extreme]
    result = indices[-1]
    return(result)

def side(input_list, side_type, length, num_type):
    list_len = len(input_list)
    if num_type == 'odd':
        odd = True
    elif num_type == 'even':
        odd = False

    length = int(length)
    nums = list(filter(lambda x: x % 2 == 0 + odd * 1, input_list))

    if length > list_len:
        return('Invalid count')
    
    if side_type == 'first':
        result = nums[:length]
    elif side_type == 'last':
        result = nums[-1::-1][:length]

    return(result)
    

user_input = input().split(' ')
user_list = list(map(int, user_input))

while True:
    user_input = input().split(' ')

    if user_input[0] == 'end':
        break

    command = user_input[0]
    args = user_input[1:]

    if command == 'exchange':
        arg = int(args[0])
        if arg + 1> len(user_list) or arg < 0:
            print('Invalid index')
            continue

        user_list = exchange(user_list, arg)
    elif command in ['max', 'min']:
        num_type = args[0]
        result = extreme(user_list, command, num_type)
        print(result)
    elif command in ['first', 'last']:
        side_type = command
        length, num_type = args[0:2]
        length = int(length)
        result = side(user_list, side_type, length, num_type)
        print(result)


print(user_list)
