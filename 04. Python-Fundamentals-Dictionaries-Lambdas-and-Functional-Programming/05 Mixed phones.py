#   Enter {name} : {phone} and correctly parse {phone} : {name}
user_input = ""
parsed = {}
alphabetical = []

while True:
    user_input = input().split(" : ")

    if user_input[0] == "Over":
        break

    item_name = user_input[0]
    item_value = user_input[1]

    try:
        int(item_value)
    except ValueError:
        item_name, item_value = item_value, item_name

    parsed[item_name] = item_value

alphabetical = sorted(parsed.keys())
for item in alphabetical:
    print("%s -> %s" % (item, parsed[item]))
