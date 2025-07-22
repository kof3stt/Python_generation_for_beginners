# Арифметические строки 🌶️
a, b, c = input(), input(), input()
if (
    len(a) == (len(b) + len(c)) / 2
    or len(b) == (len(a) + len(c)) / 2
    or len(c) == (len(a) + len(b)) / 2
):
    print("YES")
else:
    print("NO")
