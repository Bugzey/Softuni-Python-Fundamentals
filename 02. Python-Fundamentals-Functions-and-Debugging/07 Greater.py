#   Take 2 of int, char or string, return the grater of 2
def greater(in_type, two_args):
    if in_type == "int":
        for i in range(len(two_args)):
            two_args[i] = int(two_args[i])
    elif in_type == "char":
        for i in range(two_args):
            two_args[i] = two_args[i][0]
            two_args[i].title()
    elif in_type == "string":
        for i in range(two_args):
            two_args[i].title()
    else: 
        pass

    result = two_args[0]

    for i in range(two_args):
        if two_args[i] >= result:
            result = two_args[i]

    result.title()
    return(result)

input_type = input()
input_1 = input()
input_2 = input()

result = greater(input_type, [input_1, input_2])
print(result)
