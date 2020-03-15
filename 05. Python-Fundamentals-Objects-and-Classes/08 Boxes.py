#   Have boxes that have points, calculate area and perimeter
class Point:
    def __init__(self, *coords):
        self.coords = [int(item) for item in coords]
        
    def distance_to(self, other):
        if type(other) != Point:
            raise ValueError("Other point not of class point.")

        distance_list = [(self_coord - other_coord)**2 for self_coord, other_coord in zip(self.coords, other.coords)]
        distance = sum(distance_list)**(1/2)
        return(distance)

class Rectangle:
    def __init__(self, upper_left, upper_right, bottom_left, bottom_right):
        self.edges = [upper_left, upper_right, bottom_left, bottom_right]
        self.width = int(upper_left.distance_to(upper_right))
        self.height = int(upper_left.distance_to(bottom_left))

    def calc_perimeter(self):
        perimeter = int(2 * (self.width + self.height))
        return(perimeter)

    def calc_area(self):
        area = int(self.width * self.height)
        return(area)

    def __str__(self):
        area = self.calc_area()
        perimeter = self.calc_perimeter()
        out_line_1 = f'Box: {self.width}, {self.height}'
        out_line_2 = f'Perimeter: {perimeter}'
        out_line_3 = f'Area: {area}'
        result = '\n'.join([out_line_1, out_line_2, out_line_3])
        return(result)


def input_parse(user_input):
    coord_bunch = user_input.split(' | ')
    result = [item.split(':') for item in coord_bunch]
    return(result)


box_list = []
while True:
    user_input = input()
    if user_input == "end":
        print(*box_list, sep = "\n")
        break

    parsed_input = input_parse(user_input)
    point_list = [Point(*point_pair) for point_pair in parsed_input]

    cur_rectangle = Rectangle(*point_list)
    box_list.append(cur_rectangle)

