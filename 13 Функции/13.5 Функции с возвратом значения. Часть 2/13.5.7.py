# BEEGEEK 🐝🌶️
# объявление функции
def is_valid_password(password):
    numbers = password.split(":")
    return (
        len(numbers) == 3
        and is_palindrome(numbers[0])
        and is_prime(int(numbers[1]))
        and is_even(int(numbers[2]))
    )


def is_palindrome(num):
    return num == num[::-1]


def is_even(num):
    return num % 2 == 0


def is_prime(num):
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return num != 1


# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))
