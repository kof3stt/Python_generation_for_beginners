# Первое и последнее вхождение
text = input()
if text.count("f") == 1:
    print(text.index("f"))
elif text.count("f") > 1:
    print(text.index("f"), text.rindex("f"))
else:
    print("NO")
