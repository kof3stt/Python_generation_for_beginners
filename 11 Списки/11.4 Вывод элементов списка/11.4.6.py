# Negatives, Zeros and Positives
negatives, zeros, positives = list(), list(), list()
for _ in range(int(input())):
    n = int(input())
    if n > 0:
        positives.append(n)
    elif n < 0:
        negatives.append(n)
    else:
        zeros.append(n)
print(*negatives, sep="\n")
print(*zeros, sep="\n")
print(*positives, sep="\n")
