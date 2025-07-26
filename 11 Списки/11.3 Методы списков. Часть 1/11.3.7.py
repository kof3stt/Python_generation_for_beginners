# Удалите нечётные индексы
my_list = []
for _ in range(int(input())):
    my_list.append(int(input()))
del my_list[1::2]
print(my_list)
