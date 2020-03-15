#   Sort numbers and print them
nums = input().split()
nums = [int(item) for item in nums]
nums.sort()
result = " <= ".join([str(item) for item in nums])
print(result)
