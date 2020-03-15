#   Calculate the distance between two points
class Point:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

def calc_distance(point1, point2):
    delta1 = point1.x - point2.x
    delta2 = point1.y - point2.y

    distance = (delta1**2 + delta2**2)**(1/2)
    return distance

point1 = input().split()
point2 = input().split()
point1 = Point(*point1)
point2 = Point(*point2)

result = calc_distance(point1, point2)
print(f'{result:.3f}')
