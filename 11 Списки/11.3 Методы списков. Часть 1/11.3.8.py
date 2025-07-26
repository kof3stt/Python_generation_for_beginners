# k-ая буква слова 🌶️
my_list = []
for _ in range(int(input())):
    my_list.append(input())
k = int(input())
result = ""
for word in my_list:
    if len(word) >= k:
        result += word[k - 1]
print(result)
