from functools import reduce


def multiplication_my_list(var_1, var_2):
    return var_1 * var_2


my_list = [el for el in range(100, 1001, 2)]
result_multiplication = reduce(multiplication_my_list, my_list)
print(f"My_list = {my_list}")
print(f"Multiplication of list items =  {result_multiplication} ")
