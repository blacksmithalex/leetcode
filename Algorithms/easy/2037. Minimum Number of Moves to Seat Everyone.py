n = int(input())
count = 0
for _ in range(n):
    a = int(input())
    if a % 6 == 0 and a % 10 == 4:
        count += 1
print(count)