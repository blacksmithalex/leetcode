for s in range(1000):
    scopy = s
    n = 200
    while s > 0:
        s = s // 4
        n = n - 6
    if n == 170:
        print(scopy)
        break