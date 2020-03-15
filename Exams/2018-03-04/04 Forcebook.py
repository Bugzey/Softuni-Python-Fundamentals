#   Keep a database of force users
users = {}

while True:
    user_input = input()
    if user_input == 'Lumpawaroo':
        break

    if ' | ' in  user_input:
        side, user = user_input.split(' | ')

        if user not in users.keys():
            users[user] = side

    elif ' -> ' in user_input:
        user, side = user_input.split(' -> ')

        if user in users.keys():
            users[user] = side
        else:
            users[user] = side

        print(f'{user} joins the {side} side!')

sides = {side : 0  for side in users.values()}
for cur_side in sides:
    sides[cur_side] = len([user for user, side in users.items() if side == cur_side])

side_items = sorted(sides.items(), key = lambda x: (x[1], x[0]))

for cur_side in side_items:
    cur_side_members = sorted([f'! {user}' for user, side in users.items() if side == cur_side[0]])

    if cur_side[1] > 0:
        print(f'Side: {cur_side[0]}, Members: {str(cur_side[1])}')
        print(*cur_side_members, sep = '\n')

