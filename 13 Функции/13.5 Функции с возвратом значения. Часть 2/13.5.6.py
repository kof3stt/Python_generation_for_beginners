# Палиндром
# объявление функции
def is_palindrome(text):
    s = [i.lower() for i in txt if i not in ",.!?- "]
    return s == s[::-1]


# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))
