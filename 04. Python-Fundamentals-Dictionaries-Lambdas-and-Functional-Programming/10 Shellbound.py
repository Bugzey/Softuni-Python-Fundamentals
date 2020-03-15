#   Something, something shell sizes in regions
shell_list = {}
region_order = []
user_input = ""

while True:
    user_input = input().split()
    if user_input[0] == "Aggregate":
        break

    cur_region = user_input[0]
    cur_size = int(user_input[1])

    if cur_region not in region_order:
        region_order.append(cur_region)

    if cur_region not in shell_list.keys():
        shell_list[cur_region] = [cur_size]
    else:
        if cur_size in shell_list[cur_region]:
            continue
        shell_list[cur_region].append(cur_size)

giant_shells = dict.fromkeys(shell_list)
for region in region_order:
    cur_avg_shell = int(round(sum(shell_list[region]) - sum(shell_list[region]) / len(shell_list[region]), 0))
    giant_shells[region] = cur_avg_shell

    print(region + ' -> ' + ', '. join(list(map(str, shell_list[region]))) + ' (' + str(giant_shells[region]) + ')')
