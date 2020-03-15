#   Add stuff in a wardrobe, then find a specific item combination
debug = True

n_items = 0
item_list = []
item_blank_entry = \
    (None, None, None)
# item_id int, item_type str, item_colour str

def aggregate_items(item_list = item_list):
    all_items = [item[0] for item in item_list]
    all_colours = [item[1] for item in item_list]

    result = {}
    for item in all_colours:
        result[item] = {}

    for item, colour in item_list:
        if item not in result[colour].keys():
            result[colour][item] = 1
        else:
            result[colour][item] += 1

    return(result)

def format_and_highlight(colour, item, aggregated_list):
    for cur_colour in aggregated_list.keys():
        print(cur_colour + ' clothes:')
        clothes_list = aggregated_list[cur_colour].items()
        for cur_item in clothes_list:
            is_found = cur_item[0] == item and cur_colour == colour
            print('* ' + str(cur_item[0]) + ' - ' + str(cur_item[1]) + is_found * ' (found!)')

n_items = int(input())

for cur_item in range(n_items):
    user_input = input().split(' -> ')
    colour = user_input[0]
    item_types = user_input[1].split(',')
    cur_item_list = [(item_type, colour) for item_type in item_types]

    for item in cur_item_list:
        item_list.append(item)

user_input = input().split()
aggregated_list = aggregate_items()
format_and_highlight(colour = user_input[0], item = user_input[1], aggregated_list = aggregated_list)

