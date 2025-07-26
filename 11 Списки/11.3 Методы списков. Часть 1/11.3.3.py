# Алфавит
my_list = []
for i in range(ord("a"), ord("z") + 1):
    my_list.append(chr(i) * (i - 96))
print(my_list)
