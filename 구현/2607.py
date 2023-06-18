#https://www.acmicpc.net/problem/2607
from collections import Counter

n = int(input())
s = [input() for _ in range(n)]
origin = Counter(s[0])
count = 0
for i in s[1:]:
    same = Counter(i)
    if len(s[0])-len(i) >= 2:
        continue
    elif len(list((same-origin).elements())) == 0:
        count +=1
        continue
    elif len(list((same-origin).elements())) == 1 and len(list((origin-same).elements())) <= 1:
        if len(s[0]) == len(i):
            count += 1
            continue
        check = [x for i in list(i) for x in list(s[0]) if i in x]
        if check:
            count += 1
            continue
        else:
            continue
print(count)
