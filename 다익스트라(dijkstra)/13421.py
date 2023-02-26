#다익스트라 알고리즘 https://www.acmicpc.net/problem/13424
#문제 : 비밀모임

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

T= int(input())

for _ in range(T):
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
    K = int(input())
    #친구가 있는 방 위치 받기
    friend = list(map(int,input().split()))
    #각 친구가 있는 위치로 부터 각 방의 거리 합을 계산
    friends =[0 for _ in range(N+1)]
    for f in friend:
        dijkstra(f)
        friends = [i+j for i,j in zip(friends,distance)]
        visited = [0]*(N+1)
        distance = [INF]*(N+1)
    #최소가 되는 값찾기
    result = min(friends)
    #최소가 되는 방 중 가장 작은 값의 방
    print(friends.index(result))
