#https://www.acmicpc.net/problem/20040
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N,M = map(int, input().split())

def find(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if y < x:
        parent[y] = x
        return True
    elif x < y:
        parent[x] = y
        return True
    #x==y면 사이클 발생
    else:
        return False
answer = 0    
parent = [n for n in range(N)]
for i in range(M):
    x,y = map(int,input().split())
    if union(x,y):
        continue
    else:
        answer = i+1
        break
print(answer)
