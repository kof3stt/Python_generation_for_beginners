# Merge lists 1
# объявление функции
def merge(list1, list2):
    return sorted(numbers1 + numbers2)


# считываем данные
numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

# вызываем функцию
print(merge(numbers1, numbers2))
