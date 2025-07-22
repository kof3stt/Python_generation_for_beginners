# Плохие комментарии 😈
n = int(input())
for i in range(1, n + 1):
    comment = input()
    if comment.isspace() or comment == "":
        print(str(i) + ": COMMENT SHOULD BE DELETED")
    else:
        print(str(i) + ":", comment)
