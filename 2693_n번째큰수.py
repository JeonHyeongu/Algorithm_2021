import sys
t = int(sys.stdin.readline().rstrip())
for i in range(t):
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    a.sort()
    print(a[-3])
