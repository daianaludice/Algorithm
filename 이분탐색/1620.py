#https://www.acmicpc.net/problem/1620
N,M = map(int,input().split())
poketmon = []
problem = []

for i in range(N):
    poketmon.append(input())
    
pokemon = dict((y,x) for x,y in enumerate(poketmon,start=1))


for j in range(M):
    problem.append(input())

for k in problem:
    if k.isdigit():
        print(poketmon[int(k)-1])
    else:
        print(pokemon[k])
