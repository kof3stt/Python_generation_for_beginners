# Строковые минимум и максимум
word = input()
min_word = max_word = word
while word != "КОНЕЦ":
    min_word = min(min_word, word)
    max_word = max(max_word, word)
    word = input()
print("Минимальная строка ⬇️: {}".format(min_word))
print("Максимальная строка ⬆️: {}".format(max_word))
