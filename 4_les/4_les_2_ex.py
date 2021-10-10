my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(f"my_list: {my_list}")
new_list = []
el1 = my_list[0]
for el in my_list:
    if (el1 < el):
        new_list.append(el)
    el1 = el
print(f"new_list: {new_list}")
