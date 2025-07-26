# Good password 🌶️
# объявление функции
def is_password_good(password):
    digit_flag = False
    for c in password:
        if c.isdigit():
            digit_flag = True
    return (
        len(password) >= 8
        and password.lower() != password
        and password.upper() != password
        and digit_flag
    )


# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))
