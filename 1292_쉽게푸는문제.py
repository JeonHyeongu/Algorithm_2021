a, b = map(int, input().split())
arr = []
for i in range(1000):
    for j in range(i):
        arr.append(i)

index = max(a, b)
if a == b:
    print(arr[a-1])
else:
    sum_ = 0
    for i in range(a-1, b):
        sum_ += arr[i]
    print(sum_)