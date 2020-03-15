#   Hyper complex iterative string deletion
result_list = []

while True:
    state = input()
    if state == 'collapse':
        break
    fiction = input()

    while len(fiction) != 0:
        state = state.replace(fiction, '')
        fiction = fiction[1:-1]

    result_list.append(state)

print(*[item if item != '' else '(void)' for item in result_list], sep = '\n')
