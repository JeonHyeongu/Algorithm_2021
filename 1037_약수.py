import sys
n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().rstrip().split()))
a.sort()
if n % 2 == 0:
    ans = a[0] * a[-1]
else:
    ans = a[n // 2] * a[n // 2]
print(ans)