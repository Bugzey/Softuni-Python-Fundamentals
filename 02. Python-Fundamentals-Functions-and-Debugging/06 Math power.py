#   Calculate the value of a number raised to the given power
def pow(num, pow):
    result = (num**pow)
    return(result)

number = float(input())
power = float(input())

result = pow(num = number, pow = power)

print(result)
