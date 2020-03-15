#   Complicated list appending - split by "|"
nums = input().split("|")
result = list(reversed([item.split() for item in nums]))

result_print = [" ".join(item) for item in result]
print(" ".join(result_print))
