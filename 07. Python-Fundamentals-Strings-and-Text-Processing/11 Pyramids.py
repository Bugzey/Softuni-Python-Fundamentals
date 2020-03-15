#   We're filtering out pyramids
lettercount = []
max_pyramid = {}

n_lines = int(input())
lines = [input() for item in range(n_lines)]
unique_letters = set(''.join(lines))
for line in lines:
    cur_lettercount = {letter : line.count(letter) for letter in unique_letters}
    lettercount.append(cur_lettercount)

for letter in unique_letters:
    max_pyramid = {letter : 1}
    for line in lines:


print(*lettercount, sep = '\n')
