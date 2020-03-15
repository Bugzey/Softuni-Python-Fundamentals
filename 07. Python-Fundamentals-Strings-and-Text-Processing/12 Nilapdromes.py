#   Reverse the sides and core of valid nilapdromes
def find_nilaps(string):
    max_length = (len(string) + 1) // 2 
    max_side = '' 
    for item in range(max_length):
        str_left = string[:item]
        str_right = string[-item:]
        if str_left == str_right:
            max_side = str_left

    if max_side == '':
        result = None
    else:
        core = string.replace(max_side, '')
        result = core + max_side + core

    return(result)

while True:
    user_input = input()
    if user_input == 'end':
        break

    result = find_nilaps(user_input)
    if result != None:
        print(result)
