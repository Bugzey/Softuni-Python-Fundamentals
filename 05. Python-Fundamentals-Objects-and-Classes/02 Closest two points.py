#   Read N points and find the closest two fo them
from itertools import combinations

class Point:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def distance_to(self, other_point):
        if type(other_point) is not Point:
            raise TypeError('Other object is not of class Point.')
        distance = ((self.x - other_point.x)**2 + (self.y - other_point.y)**2)**(1/2)
        result = {'distance': distance, 'point1': (int(self.x), int(self.y)), 'point2': (int(other_point.x), int(other_point.y))}
        return(result)

def min_distance(*points):
    point_list = points
    nr_points = len(point_list)
    combo_indices = list(combinations(list(range(nr_points)), 2))
    combo_object = [[point_list[item1], point_list[item2]] for item1, item2 in combo_indices]
    distance_list = []
    distance_list = [pair[0].distance_to(pair[1]) for pair in combo_object]
    min_distance = min([item['distance'] for item in distance_list])
    result = [item for item in distance_list if item['distance'] == min_distance][0]
    return(result)


n_points = list(map(int, input().split()))
point_list = []

for point in range(n_points[0]):
    user_input = list(map(float, input().split()))
    cur_point = Point(*user_input)

    point_list.append(cur_point)

result = min_distance(*point_list)
result_distance = result['distance']
print(f'{result["distance"]:.3f}')
print(result['point1'])
print(result['point2'])
