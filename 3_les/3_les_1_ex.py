def division(arg_1, arg_2):
    """Выполняет деление первого аргумента на второй, делает проверку на ноль второго аргумента"""
    if (arg_2 == 0):
        return "Error. Division by zero."
    else:
        return arg_1 / arg_2


first_number= int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
print(division(first_number, second_number))