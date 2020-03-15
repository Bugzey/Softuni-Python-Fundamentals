#   Read two rectangles, discern wheter rect1 is inside rect2
class Rectangle:
    def __init__(self, *tokens):
        self.left, self.top, self.width, self.height = list(map(float, tokens))

    def is_inside(self, other_rect):
        if type(other_rect) is not Rectangle:
            raise TypeError('other_rect is not a Point object.')
        inside_horiz = self.left >= other_rect.left and self.width <= other_rect.width
        inside_verti = self.top <= other_rect.top and self.height <= other_rect.height
        fully_inside = inside_horiz and inside_verti

        result = 'Inside' if fully_inside else 'Not inside'
        return(result)

rectangle_list = []

for i in range(2):
    user_input = input().split()
    user_input = map(int, user_input)
    cur_rect = Rectangle(*user_input)
    rectangle_list.append(cur_rect)

print(rectangle_list[0].is_inside(rectangle_list[1]))
