my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result_list = []
result_list = [el for el in my_list if my_list.count(el)==1]
print(f"Result_list = {result_list}")
print(f"My_list = {my_list}")
