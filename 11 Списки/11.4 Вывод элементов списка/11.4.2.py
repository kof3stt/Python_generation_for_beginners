# Значение функции
numbers_list = []
func_list = []
for _ in range(int(input())):
    x = int(input())
    numbers_list.append(x)
    func_list.append(x**2 + 2 * x + 1)
print(*numbers_list, sep="\n", end="\n\n")
print(*func_list, sep="\n")
