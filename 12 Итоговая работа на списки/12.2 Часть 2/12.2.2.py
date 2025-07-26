# Сумма двух списков
first = [int(i) for i in input().split()]
second = [int(i) for i in input().split()]
print(*[first[i] + second[i] for i in range(len(first))])
