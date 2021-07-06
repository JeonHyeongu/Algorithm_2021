a, b = map(int, input().split())
v = 0
for i in range(min(a, b), 1, -1):
    if a % i == 0 and b % i == 0:
        v = i
        print(v)
        print((a // v) * (b // v) * v)
        break
if v == 0:
    print(1)
    print(a*b)
