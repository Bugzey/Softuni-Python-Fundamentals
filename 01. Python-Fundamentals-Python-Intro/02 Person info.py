#   Print name, age, town and salary
vars = []

for i in range(0, 4):
    vars.append(input())

print('%s is %d years old, is from %s and makes $%.1f' % (vars[0], int(vars[1]), vars[2], float(vars[3])))
#print(f'{vars[0]} is {vars[1]} years old, is from {vars[2]} and makes {vars[3]}.')
