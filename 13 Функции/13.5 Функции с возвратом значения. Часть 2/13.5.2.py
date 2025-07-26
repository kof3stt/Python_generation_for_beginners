# Is the Number Prime? 🌶️
# объявление функции
def is_prime(num):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return num != 1


# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))
