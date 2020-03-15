#   Filter some words
user_filter = input().split(' ')
user_text = input()

for cur_filter in user_filter:
    user_text = user_text.replace(cur_filter, '*' * len(cur_filter))

print(user_text)
