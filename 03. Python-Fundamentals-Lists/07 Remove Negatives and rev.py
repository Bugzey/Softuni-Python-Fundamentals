#   Remove negative numbers and reverse the list
nums = input().split()
result = list(reversed([item for item in nums if int(item) >= 0]))
if (len(result) == 0):
    print("empty")
else:
    print(' '.join(result))

