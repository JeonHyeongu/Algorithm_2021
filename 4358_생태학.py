from collections import defaultdict
import sys

a = defaultdict(int)
tree = []
while True:
    input_ = sys.stdin.readline().rstrip()
    if input_ == '':
        break
    tree.append(input_)
tree.sort()
# print(tree)

for i in tree:
    a[i] += 1
# print(a)

total = 0
name = a.keys()
count = a.values()
total = 0
for i in count:
    total += i
# print(total)

d = []
for i in name:
    d.append(i)
c = []
for i in count:
    c.append(i/total * 100)
# print(c)
# '{:.4f}'.format(i/total * 100)
for i in range(len(c)):
    print(d[i], end='')
    print(' {:.4f}'.format(c[i]))