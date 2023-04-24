def f(n):
    digits = [int(x) for x in str(n)]
    if (0 in digits) or (len(set(digits)) != len(digits)):
        return False
    for d in digits:
        if n % d != 0:
            return False
    return True

for n in range(1000, 1360):
    if f(n):
        print(n)

