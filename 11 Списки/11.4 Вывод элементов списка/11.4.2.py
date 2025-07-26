# Remove outliers
my_list = []
for _ in range(int(input())):
    my_list.append(int(input()))
del my_list[my_list.index(min(my_list))]
del my_list[my_list.index(max(my_list))]
print(*my_list, sep="\n")
