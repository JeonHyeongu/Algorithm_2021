a, b = map(int, input().split())
ans = []
min_ = 1000000000


def solve(x, num):
    global min_
    if x == b:
        if num <= min_:
            min_ = num
        return
    elif x > b:
        return
    else:
        solve(x * 2, num + 1)
        solve(x * 10 + 1, num + 1)


solve(a, 0)

if min_ == 1000000000:
    print(-1)
else:
    print(min_ + 1)
