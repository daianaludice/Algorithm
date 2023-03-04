#dfs?dp 문제 https://www.acmicpc.net/problem/17484
#문제 : 진우의 달 여행(small) 지구에서 달까지 최소연료구하기. 한번 간 방향으로 연달아 갈수 없다.
import sys
input = sys.stdin.readline
INF = int(1e9)

N,M = map(int,input().split())
dy = [-1,0,1]
graph = []
result = INF

def dfs(x,y,now):
    #달에 도달    
    if (x==N):
        return 0
    ret = INF
    for i in range(3):
        #갔던 방향은 못감
        if (now == i):
            continue
        #범위밖이면 pass
        if (y+dy[i]<0 or y+dy[i] >=M):
            continue
        ret = min(ret,dfs(x+1,y+dy[i],i)+graph[x][y])
    return ret
    
            
for _ in range(N):
    g = list(map(int,input().split()))
    graph.append(g)

for m in range(M):
    result = min(result,dfs(0,m,-1))
print(result)
