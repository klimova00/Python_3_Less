def my_func_summ_numbers():
    result = 0
    while True:
        my_func_list = input("Enter numbers separated by space or enter EOF to exit ").upper().split()
        for i in my_func_list:
            if i == 'EOF':
                print(f"Finish result = {result}. goodbye.")
                return -1
            try:
                result += int(i)
            except ValueError:
                print("You only need to enter numbers")
                print(result)
        else:
            print(result)
            continue
        break
    return result


my_func_summ_numbers()
