# Самое тяжёлое слово 🗿
heaviest_word = ""
heaviest_weight = 0
for _ in range(4):
    word = input()
    word_weight = 0
    for c in word:
        word_weight += ord(c)
    if word_weight > heaviest_weight:
        heaviest_weight = word_weight
        heaviest_word = word
print(heaviest_word)
