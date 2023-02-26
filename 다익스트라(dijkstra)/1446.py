#다익스트라 알고리즘 https://www.acmicpc.net/problem/1446
#문제 : 지름길 일렬로 되어있는 길에 지름길의 개수 N개와 고속도리의 길이D -> D가 도착해야하는 값으로 봐야한다. 지름길 일렬로 되어있는 값으
#굳이 다익스트라로 풀 필요 X

import sys
import heapq
input = sys.stdin.readline

N, D = map(int, input().split())
distance = [i for i in range(10001)]
graph = []

for _ in range(N):
    s,e,c = map(int,input().split())
    heapq.heappush(graph,(s,e,c))
    
while graph:
    S,E,C = heapq.heappop(graph)
    # 만약 지름길이 고속도로보다 오래걸리거나, 도착지점을 지나치면(역주행불가) 패스
    if C > (distance[E]-distance[S]) or E > D:
        continue
        
    #지름길로 갈경우 거리 계산하여 갱신
    cost  = distance[S]+C
    distance[E] = cost
    
    #지름길를 통해 가는걸로 갱신, 다른 지름길과도 비교하여 더 빠르값으로 갱신되게min사용
    for i in range(E+1,10001):
        distance[i] = min(distance[i-1]+1,distance[i])

print(distance[D])
