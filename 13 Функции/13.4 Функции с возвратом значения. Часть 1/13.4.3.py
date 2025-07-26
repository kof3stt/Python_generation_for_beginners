# Делители 1
# объявление функции
def get_factors(num):
    return [i for i in range(1, n + 1) if n % i == 0]


# считываем данные
n = int(input())

# вызываем функцию
print(get_factors(n))
