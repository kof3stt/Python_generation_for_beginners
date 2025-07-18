# Високосный год 📅
year = int(input())
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("YES")
else:
    print("NO")
