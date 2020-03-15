#   Reads a list of integers
num_iterations = int(input())
list_items = []

for element in range(num_iterations):
    list_items.append(int(input()))

result = 0
for element in list_items:
    result += element

print(result)
