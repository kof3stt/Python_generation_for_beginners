# Самописный калькулятор 🌶️
operand1, operand2, operator = int(input()), int(input()), input()
if operator == "+":
    print(operand1 + operand2)
elif operator == "-":
    print(operand1 - operand2)
elif operator == "*":
    print(operand1 * operand2)
elif operator == "/":
    if operand2 == 0:
        print("На ноль делить нельзя!")
    else:
        print(operand1 / operand2)
else:
    print("Неверная операция")
