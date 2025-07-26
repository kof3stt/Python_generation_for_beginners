# Найти всех
# объявление функции
def find_all(target, symbol):
    return [i for i in range(len(s)) if s[i] == char]


# считываем данные
s = input()
char = input()

# вызываем функцию
print(find_all(s, char))
