# Четырёхзначное число
n = int(input())
d1 = (n % 10**4) // 10**3
d2 = (n % 10**3) // 10**2
d3 = (n % 10**2) // 10**1
d4 = (n % 10**1) // 10**0
print("Цифра в позиции тысяч равна", d1)
print("Цифра в позиции сотен равна", d2)
print("Цифра в позиции десятков равна", d3)
print("Цифра в позиции единиц равна", d4)
