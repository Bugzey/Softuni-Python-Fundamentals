#   Get the sign of an integer
def get_sign(num):
    if num > 0:
        print('The number %d is positive.' % (num))
    elif num < 0:
        print('The number %d is negative.' % (num))
    else:
        print('The number %d is zero.' % (num))


input_num = int(input())

get_sign(input_num)
