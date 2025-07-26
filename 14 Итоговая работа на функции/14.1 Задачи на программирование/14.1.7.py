# Панграммы 🌶️
from string import ascii_lowercase


# объявление функции
def is_pangram(text):
    for c in ascii_lowercase:
        if c not in text.lower():
            return False
    return True


# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))
