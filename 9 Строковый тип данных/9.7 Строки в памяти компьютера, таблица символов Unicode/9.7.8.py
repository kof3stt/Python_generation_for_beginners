# Сбой в системе ⚠️🌶️
text = input()
for i in range(ord("А"), ord("я") + 1):
    text = text.replace(f"[u-{i}]", chr(i))
print(text)
