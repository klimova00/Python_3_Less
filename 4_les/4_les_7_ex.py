def my_factorial_gen(var_1):
    first = 1
    if var_1 == 0:
        print(f"Factorial{var_1} = 1")
    for i in range(1, var_1 + 1):
        first = first * i
        yield f"Factorial {i} = {first}"


my_number = int(input("Enter factorial number:"))
for el in my_factorial_gen(my_number):
    print(el)
