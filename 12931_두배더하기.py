#두 배 더하기 - 12931
n = int(input())
a = [0] * n
b = list(map(int, input().split()))
b.sort()
cnt = 0


def solve():
    global cnt
    if b != a:
        flag = True
        for i in range(len(b)):
            if b[i] % 2 != 0:
                b[i] -= 1
                cnt += 1
                flag = False
        if b == a:
            return
        else:
            if flag == True:
                for i in range(len(b)):
                    b[i] = b[i] / 2
                cnt += 1
            if b == a:
                return
            else:
                solve()
    else:
        return


solve()
print(cnt)