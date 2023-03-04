#구현 https://www.acmicpc.net/problem/1157
#문제 : 단어공부
import sys
from collections import Counter
input = sys.stdin.readline

S = input().upper()
most = Counter(S).most_common()

if len(S)==1:
    print(S)
elif most[0][1] == most[1][1] and len(S)>2:
    print('?')      
else:
    print(most[0][0])
