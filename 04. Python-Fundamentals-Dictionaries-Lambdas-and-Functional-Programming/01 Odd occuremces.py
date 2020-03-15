#   Extract all elements that are present an odd number of times
nums = input().split()
result = {}

for item in nums:
    element = item.lower()
    if element in result.keys():
        result[element] += 1
    else:
        result[element] = 1

result_print = []
for key, item in result.items():
    if item %2 == 1:
        result_print.append(key)

print(*result_print, sep = ", ")
