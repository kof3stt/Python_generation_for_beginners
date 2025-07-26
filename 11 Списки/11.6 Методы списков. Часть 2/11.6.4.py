# Взлом Братства Стали 🌶️
n = int(input()[1:])
for i in range(n):
    line = input()
    if "#" in line:
        line = line[: line.find("#")]
    print(line.rstrip())
