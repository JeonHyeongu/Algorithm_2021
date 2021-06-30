# 양념반 후라이드반 - 16917
a, b, c, x, y = map(int, input().split())
cnt = max(x * 2, y * 2)

ans = []
for i in range(cnt):
    q = a * (x-i)
    w = b * (y-i)
    e = c * i * 2
    if q < 0:
        q = 0
    if w < 0:
        w = 0
    ans.append(q + w + e)
print(min(ans))