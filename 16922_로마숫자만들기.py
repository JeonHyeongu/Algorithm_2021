n = int(input())
num = [1, 5, 10, 50] * n
ans = []
for a in range(n+1):
    for b in range(n-a+1):
        for c in range(n-a-b+1):
            d = n - (a+b+c)
            sum_ = a * 1 + b * 5 + c * 10 + d * 50
            if sum_ not in ans:
                ans.append(sum_)
print(len(ans))