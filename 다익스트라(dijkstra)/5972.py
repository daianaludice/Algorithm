#다익스트라 알고리즘 https://www.acmicpc.net/problem/5972
#문제 : 택배 배송 , 출발지 1에서 양방향 길 여러길을 통해 N까지 가는 최소구하기.

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)
distance = [INF]*(N+1)

for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dijkstra(start):
    queue = []
    #시작정보 큐에 삽입
    heapq.heappush(queue,(0,start))
    distance[start]= 0
    while queue:
        dist,node = heapq.heappop(queue)
        #거리가 이미 갱신된 거리보다 클 경우 패스
        if distance[node] < dist:
            continue
        # 현재 노드에서 인접한 노드들 탐색
        for next in graph[node]:
            # cost는 시작거리에서 현재 node와의 거리 + 탐색중인 인접노드와의 거리
            cost = distance[node]+next[1]
            #방문을 안했으면 cost 넣고, 방문을 했어도 기존보다 작은 값이면 갱신
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                #갱신했기때문에 위치변경하고 계속진행
                heapq.heappush(queue,(cost,next[0]))
#출발점이 1로고정                
dijkstra(1)

#도착지 N에서의 값이 최소거리값
print(distance[N])
