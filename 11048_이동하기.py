n, m = map(int, input().split())
a = [([0] + list(map(int, input().split()))) for _ in range(n)]
a = [[0] * (m+1)] + a
# print(a)
d = [[0] * (m+1) for _ in range(n+1)]
# print(d)

for i in range(1, n+1):
    for j in range(1, m+1):
        d[i][j] = a[i][j] + max(d[i-1][j], d[i][j-1], d[i-1][j-1])

print(d[n][m])