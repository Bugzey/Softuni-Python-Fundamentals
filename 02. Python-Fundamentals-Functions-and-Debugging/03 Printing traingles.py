#   Print a triangle
def print_triangle(end, start=1):
    for i in range(start, end + 1):
        print(i, end = ' ')
    print()

input_num = int(input())

for i in range(input_num):
    print_triangle(i)

for i in range(input_num, 0, -1):
    print_triangle(i)
