# Google search - 1
my_list = []
for _ in range(int(input())):
    my_list.append(input())
request = input()
for string in my_list:
    if request.lower() in string.lower():
        print(string)
