# Валидный номер 📞🌶️🌶️
phone_num = input().split("-")
flag = "YES"
if not 3 <= len(phone_num) <= 4:
    flag = "NO"
elif len(phone_num) == 4 and phone_num[0] != "7":
    flag = "NO"
if len(phone_num) == 4:
    del phone_num[0]
for i in range(len(phone_num)):
    if i < 2 and len(phone_num[i]) != 3 or not phone_num[i].isdigit():
        flag = "NO"
    elif i == 2 and len(phone_num[i]) != 4 or not phone_num[i].isdigit():
        flag = "NO"
print(flag)
