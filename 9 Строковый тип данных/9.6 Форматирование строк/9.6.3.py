# (Не) Активное похудение 🏃🌶️
day, weight = int(input()), float(input())
flag = "Все идет по плану"
if 100 - 0.2 * day < weight:
    flag = "Что-то пошло не так"
print(
    flag,
    f"#{day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {weight} кг, ЦЕЛЬ по ВЕСУ = {100 - 0.2 * day} кг",
    sep="\n",
)
