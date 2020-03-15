#   Calculate the needed sum for equipment
from math import ceil

price = {
    'lightsaber': 0, 
    'robe': 0, 
    'belt': 0
}
cash = 0
n_students = 0

user_input = [input() for item in range(5)]

cash = float(user_input[0])
n_students = int(user_input[1])
price['lightsaber'] = float(user_input[2])
price['robe'] = float(user_input[3])
price['belt'] = float(user_input[4])

cash_needed = \
    ceil(n_students * 1.1) * price['lightsaber'] + \
    n_students * price['robe'] + \
    (n_students - n_students // 6) * price['belt']

if cash_needed > cash:
    result = f'Ivan Cho will need {cash_needed - cash:.2f}lv more.' 
else:
    result = f'The money is enough - it would cost {cash_needed:.2f}lv.'

print(result)
