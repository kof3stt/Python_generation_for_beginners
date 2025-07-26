# Переставить min и max
numbers = input().split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
min_elem_ind = numbers.index(min(numbers))
max_elem_ind = numbers.index(max(numbers))
numbers[min_elem_ind], numbers[max_elem_ind] = (
    numbers[max_elem_ind],
    numbers[min_elem_ind],
)
print(*numbers)
