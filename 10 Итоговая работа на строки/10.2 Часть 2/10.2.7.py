# Каждый третий 3️⃣
s = input()
for i in range(len(s)):
    if i != 0 and i % 3 != 0:
        print(s[i], end="")
