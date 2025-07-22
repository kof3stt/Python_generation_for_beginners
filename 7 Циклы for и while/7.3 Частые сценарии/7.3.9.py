# Наибольшие числа 🌶️🌶️
first_largest = second_largest = 0
for i in range(int(input())):
    n = int(input())
    if n > first_largest:
        second_largest = first_largest
        first_largest = n
    elif n > second_largest:
        second_largest = n
print(first_largest, second_largest, sep="\n")
