#   Traingle area
def calc_area(a, b):
    result = (a * b / 2)
    if result % 1 == 0:
        result = int(result)
    return result

side1 = float(input())
side2 = float(input())

print(calc_area(side1, side2))

