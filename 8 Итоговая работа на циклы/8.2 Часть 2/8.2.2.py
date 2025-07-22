# Ревью кода-8 🌶️
n = 8
count = 0
maximum = -9999999999999999
for i in range(1, n + 1):
    x = int(input())
    if x % 4 == 0:
        count += 1
        if x >= maximum:
            maximum = x
if count > 0:
    print(count)
    print(maximum)
else:
    print("NO")
