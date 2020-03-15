#   Receive input {item} = {value}, parse and retreive
cur_input = ""
parsed = {}
input_history = []

while True:
    cur_input = input().split(" = ")
    if cur_input[0] == "end":
        break

    item_name = cur_input[0]
    item_value = cur_input[1]

    try:
        item_value_int = int(item_value)
    except ValueError:
        if item_value not in parsed.keys():
            continue
        
    if item_name not in parsed.keys():
        input_history.append(item_name)

    if item_value in parsed.keys():
        parsed[item_name] = parsed[item_value]
    else:
        parsed[item_name] = int(item_value)

#print(parsed)
#print(*input_history)
for item in input_history:
    print("%s === %d" % (item, parsed[item]))
