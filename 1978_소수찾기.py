n = int(input())
a = list(map(int, input().split()))
cnt = 0
for i in range(n):
    x = a[i]
    flag = True
    if x >= 4:
        for j in range(2, x-1):
            if x % j == 0:
                flag = False
                break
        if flag == True:
            cnt += 1
    elif x == 2 or x == 3:
        cnt += 1

print(cnt)
