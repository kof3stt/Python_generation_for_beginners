# Суммы двух
my_list = []
total = 0
for _ in range(int(input())):
    n = int(input())
    total += n
    my_list.append(total)
    total = n
del my_list[0]
print(my_list)
