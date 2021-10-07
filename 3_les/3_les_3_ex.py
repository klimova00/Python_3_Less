def my_func(var_1, var_2, var_3):
    try:
        sum_all = sum((var_1, var_2, var_3))
        return sum_all - min(var_1, var_2, var_3)
    except TypeError:
        return "You only need to enter numbers"


print(my_func(6, 5, 4))
print(my_func("Hello", 3, 5))
