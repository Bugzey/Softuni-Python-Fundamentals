#   Count the odd numbers in an input list
nums = [int(item) for item in input().split()]
result = len([item for item in nums if item % 2 != 0])
print(result)
