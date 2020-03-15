#   Read an integer and multiply the sum of its evens
#       by that of its odds

def multiply(number):
    number = str(number)
    num_length = len(number)
    odds = range(0, num_length, 2)
    evens = range(1, num_length, 2)
    sum_odds = 0
    sum_evens = 0

    for i in odds:
        sum_odds += int(number[i])
    for i in evens:
        sum_evens += int(number[i])
    result = sum_odds * sum_evens
    return(result)

in_number = abs(int(input()))

result = multiply(in_number)
print(result)
