#   Get a list of space-separated input ints. Multiply a new input
nums = input().split()
multiplier = int(input())

result = [int(item) * multiplier for item in nums]

for item in result:
    print(item, end = ' ')
print()

