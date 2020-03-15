#   Draw a filled-in square
def print_edge(side_length):
    print('-' * side_length * 2)


def print_mid(side_length):
    for i in range(side_length - 2):
        print('-' + '\/' * (side_length - 1)  + '-')


num = int(input())
print_edge(num)
print_mid(num)
print_edge(num)
