# Количество артиклей
text = input().lower().split()
total_articles = text.count("a") + text.count("an") + text.count("the")
print("Общее количество артиклей:", total_articles)
