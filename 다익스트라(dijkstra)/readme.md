다익스트라(dijkstra) 알고리즘
-> 최단경로 알고리즘
: graph 구조를 사용하여 노드와 가중치를 가진 간선 을 이용하여 실제 거리를 표현한다.
이를 위해 아래의 과정을 거친다

1. 출발 노드와, 도착 노드를 설정
2. 그래프를 생성하여 알고 있는 모든 거리 값을 부여
3. 출발 노드부터 시작하여, 방문하지 않은 인접 노드를 방문, 거리를 계산한 다음, 현재 알고있는 거리보다 짧으면 해당 값으로 갱신한다.
4. 현재 노드에 인접한 모든 미방문 노드까지의 거리를 계산했다면, 현재 노드는 방문한 것이므로, 미방문 집합에서 제거한다.
5. 도착 노드가 미방문 노드 집합에서 벗어나면, 알고리즘을 종료한다.

point) 우선순위 큐를 사용 하면, 지금까지 발견된 가장 짧은 거리의 노드에 대해서 먼저 계산할 수 있으며, 더 긴 거리로 계산 되었을 시 스킵한다

[기본적인 틀]

import heapq  # 우선순위 큐 구현을 위함

def dijkstra(graph, start):
  distances = {node: float('inf') for node in graph}  # start로 부터의 거리 값을 저장하기 위함
  distances[start] = 0  # 시작 값은 0이어야 함
  queue = []
  heapq.heappush(queue, [distances[start], start])  # 시작 노드부터 탐색 시작 하기 위함.

  while queue:  # queue에 남아 있는 노드가 없으면 끝
    current_distance, current_destination = heapq.heappop(queue)  # 탐색 할 노드, 거리를 가져옴.

    if distances[current_destination] < current_distance:  # 기존에 있는 거리보다 길다면, 볼 필요도 없음
      continue
    
    for new_destination, new_distance in graph[current_destination].items():
      distance = current_distance + new_distance  # 해당 노드를 거쳐 갈 때 거리
      if distance < distances[new_destination]:  # 알고 있는 거리 보다 작으면 갱신
        distances[new_destination] = distance
        heapq.heappush(queue, [distance, new_destination])  # 다음 인접 거리를 계산 하기 위해 큐에 삽입
    
  return distances
  
  출처 : https://justkode.kr/algorithm/python-dijkstra
  
