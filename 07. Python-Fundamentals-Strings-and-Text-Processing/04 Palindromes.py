#   ABBA reversed is ABBA, print all such palindromes
user_input = input().split()
result = [word for word in user_input if word == word[::-1]]
result = list(set(result))
#result.sort(key = str.lower)
result.sort(key = str.upper)
print(*result, sep = ', ')

