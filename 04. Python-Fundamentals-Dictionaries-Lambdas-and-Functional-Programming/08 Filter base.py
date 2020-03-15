#   Free-form data entry and type-based filtering
#list_age = {}
#list_salary = {}
#list_position = {}
full_list = {}
list_item = {
        'Age': None,
        'Salary': None,
        'Position': None
}
names = []
full_input_order = {
        'Age' : [],
        'Salary' : [],
        'Position' : []
}

status_options = ['entry', 'retreival']
status = status_options[0]

def add_info(user, item):
    if user not in names:
        names.append(user)
        full_list[user] = dict.fromkeys(list_item)
    try:
        item = int(item)
        full_list[user]['Age'] = item
        full_input_order['Age'].append(user)
        return(0)
    except ValueError:
        pass

    try:
        item = float(item)
        full_list[user]['Salary'] = item
        full_input_order['Salary'].append(user)
        return(0)
    except ValueError:
        pass

    full_list[user]['Position'] = item
    full_input_order['Position'].append(user)
    return(0)

def print_db(db):
    result = {item : str(value[db]) for item, value in full_list.items() if full_list[item][db] != None}
    #print(*result.items(), sep = '\n')
    for item in full_input_order[db]:
        print('Name: ' + item + '\n' + db + ': ' + result[item])
        print(20 * '=')

while True:
    user_input = input().split(' -> ')
    
    if user_input[0] == 'filter base':
        status = status_options[1]
        continue
    elif len(user_input) in [0, 1] and user_input[0] not in list_item.keys():
        continue

    if status == status_options[0]:
        input_name = user_input[0]
        input_item = user_input[1]

        add_info(input_name, input_item)
    elif status == status_options[1]:
        print_db(user_input[0])
        break
