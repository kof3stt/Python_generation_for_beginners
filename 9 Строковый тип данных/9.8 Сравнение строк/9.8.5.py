# Сортируем слова 📶
word1, word2, word3 = input(), input(), input()
if word1 < word2 and word1 < word3:
    print(word1, end=" ")
    if word2 < word3:
        print(word2, word3)
    else:
        print(word3, word2)
elif word2 < word1 and word2 < word3:
    print(word2, end=" ")
    if word1 < word3:
        print(word1, word3)
    else:
        print(word3, word1)
else:
    print(word3, end=" ")
    if word2 < word1:
        print(word2, word1)
    else:
        print(word1, word2)
