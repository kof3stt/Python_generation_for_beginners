# Порядок книг 📚🌶️
prev_book = ""
is_ordered = "YES"
for i in range(int(input())):
    book = input()
    surname = book[: book.find(" ")]
    title = book[book.find("«") + 1 : book.find("»")]
    current_book = surname + title
    if current_book < prev_book:
        is_ordered = "NO"
    prev_book = current_book
print(is_ordered)
