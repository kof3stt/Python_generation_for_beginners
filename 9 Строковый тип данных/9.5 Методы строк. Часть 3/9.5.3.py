# Проверь никнейм 👩🌶️
name = input()
flag = "Correct"
if (
    name[0] != "@"
    or not 5 <= len(name) <= 15
    or not name[1:].isalnum()
    or name.lower() != name
):
    flag = "Incorrect"
print(flag)
