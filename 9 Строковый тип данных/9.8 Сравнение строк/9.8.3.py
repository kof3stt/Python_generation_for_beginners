# Название класса 👩‍🏫🌶️
for _ in range(int(input())):
    classname = input()
    if (
        len(classname) == 2
        and "0" <= classname[0] <= "9"
        and "А" <= classname[1] <= "П"
    ):
        print("YES")
    else:
        print("NO")
