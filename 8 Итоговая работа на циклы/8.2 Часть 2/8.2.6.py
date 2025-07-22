# Все вместе 2
n = int(input())
count_3 = count_last_digit = count_even = total_digits_more_5 = total_zero_five = 0
product_digits_more_7 = 1
last_digit = n % 10
while n > 0:
    curr_digit = n % 10
    if curr_digit == 3:
        count_3 += 1
    if curr_digit == last_digit:
        count_last_digit += 1
    if curr_digit % 2 == 0:
        count_even += 1
    if curr_digit > 5:
        total_digits_more_5 += curr_digit
    if curr_digit == 0 or curr_digit == 5:
        total_zero_five += 1
    if curr_digit > 7:
        product_digits_more_7 *= curr_digit
    n //= 10
print(
    count_3,
    count_last_digit,
    count_even,
    total_digits_more_5,
    product_digits_more_7,
    total_zero_five,
    sep="\n",
)
