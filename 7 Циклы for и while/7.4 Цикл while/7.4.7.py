# Ведьмаку заплатите чеканной монетой 💰
n = int(input())
total = 0
while n >= 25:
    total += 1
    n -= 25
while n >= 10:
    total += 1
    n -= 10
while n >= 5:
    total += 1
    n -= 5
while n >= 1:
    total += 1
    n -= 1
print(total)
