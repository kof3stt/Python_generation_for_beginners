# Ход коня ♘
x1, y1 = int(input()), int(input())
x2, y2 = int(input()), int(input())
if (
    (x1 - x2) ** 2 == 4
    and (y1 - y2) ** 2 == 1
    or (x1 - x2) ** 2 == 1
    and (y1 - y2) ** 2 == 4
):
    print("YES")
else:
    print("NO")
