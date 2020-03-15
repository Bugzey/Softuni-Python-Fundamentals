#   Print a list of real numbers in ascending order
nums = input().split()

counts = {}

for item in nums:
    if item in counts.keys():
        counts[item] += 1
    else:
        counts[item] = 1

ordered_keys = sorted([float(item) for item in counts.keys()])

result = []
for item in ordered_keys:
    if item %1 == 0:
        new_item = str(int(item))
    else:
        new_item = str(item)
    result.append(new_item)

for item in result:
    print("%s -> %d times" % (float(item), counts[item]))

