from itertools import count
from itertools import cycle

print("итератор, генерирующий целые числа, начиная с указанного. Для выхода введите EOF. ")
for i in count(int(input("Enter start number: "))):
    print(i)
    end = input()
    if end == "EOF":
        break
print("итератор, повторяющий элементы некоторого списка, определенного заранее. Для выхода введите EOF.")
my_list = [1, 4, 3, 2, 7, 10, 22, 45, 23, 55]
iteration = cycle(my_list)
end = input()

while end != "EOF":
    print(next(iteration))
    end = input()
