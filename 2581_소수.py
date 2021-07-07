m = int(input())
n = int(input())
a = [2]
for i in range(3, n+1):
    flag = True
    for j in range(2, i-1):
        if i % j == 0:
            flag = False
            break
    if flag == True:
        a.append(i)
min_ = 100000
total = 0
for i in range(len(a)):
    if m <= a[i] <= n:
        total += a[i]
        if a[i] < min_:
            min_ = a[i]
if total == 0:
    print(-1)
else:
    print(total)
    print(min_)