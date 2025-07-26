# Next Prime 🌶️
# объявление функции
def is_prime(num):
    while True:
        num += 1
        total = 0
        for i in range(2, num):
            if num % i == 0:
                total += 1
                break
        if total == 0:
            return num


# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))
