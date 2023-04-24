def f(x, y, p):
    if x + y >= 62 and (p == 5 or p == 3):
        return True
    elif x + y < 62 and p == 5:
        return False
    elif x + y >= 62:
        return False
    else:
        if p % 2 == 0:
            return f(x + 2, y, p + 1) or f(x, y + 2, p + 1) or f(x * 2, y, p + 1) or f(x, y * 2, p + 1)
        else:
            return f(x + 2, y, p + 1) and f(x, y + 2, p + 1) and f(x * 2, y, p + 1) and f(x, y * 2, p + 1)

for S in range(1, 54 + 1):
    if f(7, S, 1):
        print(S)