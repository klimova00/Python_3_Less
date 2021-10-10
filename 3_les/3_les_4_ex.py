def my_func_1(x, y):
    try:
        x = float(x)
        y = int(y)
    except ValueError:
        return "x must be float_type, y must be int_type"
    if y >= 0 or x <= 0:
        return "y must be negative and x must be positive"
    return x ** y


def my_func_2(x, y):
    try:
        x = float(x)
        y = int(y)
    except ValueError:
        return "x must be float_type, y must be int_type"
    if y >= 0 or x <= 0:
        return "y must be negative and x must be positive"
    res = 1
    for _ in range(abs(y)):
        res = res * x
    result = 1 / res
    return result


print(my_func_1(2, -3))
print(my_func_2(2, -3))
