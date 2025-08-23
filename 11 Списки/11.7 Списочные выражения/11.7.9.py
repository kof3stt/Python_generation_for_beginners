# В одну строку 3
print(
    *[int(i) ** 2 for i in input().split() if int(i) ** 2 % 10 != 4 and int(i) % 2 == 0]
)
