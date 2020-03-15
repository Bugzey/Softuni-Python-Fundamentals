#   Receive string manipulation commands
def move_left(count):
    count -= (count // len(input_string)) * len(input_string)
    result = input_string[count:] + input_string[:count]
    return(result)

def move_right(count):
    count -= (count // len(input_string)) * len(input_string)
    #result = input_string[:count] + input_string[count:] 
    result = input_string[-count:] + input_string[:-count]
    return(result)

def insert(index, string):
    result = input_string[:index] + string + input_string[index:]
    return(result)

def delete(start, end):
    result = input_string[:start] + input_string[end + 1:]
    return(result)

input_string = input()

while True:
    user_input = input().split(' ')

    if user_input[0] == 'end':
        break

    command, arguments = user_input[0], user_input[1:]
    if command in ['Left', 'Right']:
        arguments[0] = int(arguments[0])
        if command == 'Left':
            input_string = move_left(arguments[0])
        elif command == 'Right':
            input_string = move_right(arguments[0])
    elif command == 'Insert':
        arguments[0] = int(arguments[0])
        input_string = insert(arguments[0], arguments[1])
    elif command == 'Delete':
        arguments = list(map(int, arguments))
        input_string = delete(arguments[0], arguments[1])
    else:
        print(f'Unknown command {command}')

print(input_string)
