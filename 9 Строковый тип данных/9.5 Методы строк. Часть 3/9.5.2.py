# Автомобильный номер 🚘🌶️
num = input()
alphabet = "АВЕКМНОРСТУХ"
flag = "YES"
if len(num) != 9 and len(num) != 10:
    flag = "NO"
if (
    num[0] not in alphabet
    or not num[1:4].isdigit()
    or not num[4] in alphabet
    or not num[5] in alphabet
    or not num[6] == "_"
    or not num[7:].isdigit()
):
    flag = "NO"
print(flag)
