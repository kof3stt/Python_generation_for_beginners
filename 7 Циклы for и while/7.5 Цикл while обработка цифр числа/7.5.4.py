# Все вместе
num = int(input())
sum_digits = total_digits = arithmetic_mean = first_digit = sum_first_last_digit = 0
product_digits = 1
while num > 0:
    last_digit = num % 10
    sum_digits += last_digit
    total_digits += 1
    product_digits *= last_digit
    first_digit = last_digit
    if total_digits == 1:
        sum_first_last_digit += last_digit
    num //= 10
sum_first_last_digit += first_digit
arithmetic_mean = sum_digits / total_digits
print(
    sum_digits,
    total_digits,
    product_digits,
    arithmetic_mean,
    first_digit,
    sum_first_last_digit,
    sep="\n",
)
