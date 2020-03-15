#   Read a list and rotate it to the right
input_items = input().split()
result = [input_items[-1]] + input_items[0:-1]

for item in result:
    print(item, end = ' ')
print()
