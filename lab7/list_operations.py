my_list = [1, 10, 7, 6, 3, 32,-1, 11, 8]

def list_operation(parameter, my_list):
    return parameter(my_list)

print(list_operation(sum, my_list))
print(list_operation(len, my_list))