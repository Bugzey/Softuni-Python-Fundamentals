#   Print the nr. of times a letter was printed
user_input = input()

counts = {}
for letter in user_input:
    if letter in counts.keys():
        counts[letter] += 1
    else:
        counts[letter] = 1

for item, key in counts.items():
    print("%s -> %s" % (item, key))
