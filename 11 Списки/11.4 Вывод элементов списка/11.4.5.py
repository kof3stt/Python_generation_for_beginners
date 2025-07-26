# Google search - 2 🌶️
my_list = []
for _ in range(int(input())):
    my_list.append(input())
requests = []
for _ in range(int(input())):
    requests.append(input())
for string in my_list:
    flag = True
    for req in requests:
        if req.lower() not in string.lower():
            flag = False
            break
    if flag:
        print(string)
