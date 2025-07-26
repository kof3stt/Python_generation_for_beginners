# Сумма чисел
data = [i for i in input().split()]
print(f"{"+".join(data)}={sum([int(i) for i in data])}")
