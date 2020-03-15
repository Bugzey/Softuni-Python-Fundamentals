#   Print the square numbers from an input list
nums = input().split()
#result = [str(item) for item in nums if float(item)**(1/2) %1 == 0].sort()
result = [int(item) for item in nums if float(item) >= 0 and abs(float(item))**(1/2) %1 == 0.0]
result.sort(reverse=True)
print(" ".join([str(item) for item in result]))
#print(result)
