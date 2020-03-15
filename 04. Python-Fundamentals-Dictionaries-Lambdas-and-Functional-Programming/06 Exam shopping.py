#   Stock up a shop and keep track of purchases
stock = {}
user_input = ""

states = ['stock', 'shop', 'end']

cur_state = states[0]

while True:
    user_input = input().split()
    user_command = user_input[0]

    if user_command == 'shopping':
        cur_state = states[1]
        continue
    if user_command == 'exam':
        cur_state = states[2]
        break

    if (len(user_input) < 3):
        #print('Invalid input')
        continue

    user_item = user_input[1]
    user_quantity = int(user_input[2])

    if user_command == 'stock' and cur_state == states[0]:
        if user_item not in stock.keys():
            stock[user_item] = 0
        stock[user_item] += user_quantity
    elif user_command == 'buy' and cur_state == states[1]:
        if user_item not in stock.keys():
            print(f'{user_item} doesn\'t exist')
            continue

        if stock[user_item] <= 0:
            print(f'{user_item} out of stock')
            continue

        stock[user_item] -= min(user_quantity, stock[user_item])
    else:
        #print('Invalid command or state.')
        continue
        
ordered_stock = filter(lambda key: stock[key] > 0, stock.keys())
for item in ordered_stock:
    print(f'{item} -> {stock[item]}')

