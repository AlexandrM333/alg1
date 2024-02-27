def F(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n > 2:
        return 2 * F(n-1) + (n-2) * F(n-2)
print(F(6))