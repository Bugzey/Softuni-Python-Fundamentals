#   Ho many odd numbers at odd positions there are
user_input = input().split()
nums = enumerate([int(item) for item in user_input])
result = [(item_nr, item) for (item_nr, item) in nums if (item_nr % 2 != 0 and item % 2 != 0)]

for result_set in result:
    print("Index %d -> %d" % (result_set[0], result_set[1]))

