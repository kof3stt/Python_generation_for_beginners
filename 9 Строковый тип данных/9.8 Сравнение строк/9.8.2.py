# Волшебное число ✨
min_word = max_word = input()
for _ in range(3):
    word = input()
    if word < min_word:
        min_word = word
    if word > max_word:
        max_word = word
print((ord(min_word[-1]) * ord(max_word[-1])) ** 2)
