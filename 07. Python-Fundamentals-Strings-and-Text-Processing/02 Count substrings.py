#   Count the number of substring occurences
user_input = input().lower()
search_term = input().lower()

count = 0
cur_index = 0

while True:
    try:
        cur_index = user_input.index(search_term, cur_index)
    except ValueError:
        break
    count += 1
    cur_index += 1

print(count)
