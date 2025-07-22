# Три города 🏙️
a, b, c = input(), input(), input()
if len(a) <= len(b) and len(a) <= len(c):
    print(a)
elif len(b) <= len(a) and len(b) <= len(c):
    print(b)
elif len(c) <= len(a) and len(c) <= len(b):
    print(c)
if len(a) >= len(b) and len(a) >= len(c):
    print(a)
elif len(b) >= len(a) and len(b) >= len(c):
    print(b)
elif len(c) >= len(a) and len(c) >= len(b):
    print(c)
