#https://www.acmicpc.net/problem/1987
#문제 : 알파벳 유형 : 그래프 탐색, 깊이우선탐색,백트래킹
# 15:44 ~16:32 bfs풀이 시간초과
import sys
from collections import deque

input = sys.stdin.readline
R,C = map(int,input().split())
graph = [list(input()) for _ in range(R)]
#출발점부터 카운트
cnt = 1

    
def bfs(x,y):
    global cnt
    queue = deque()
    queue.append([x,y,graph[x][y]])
    while queue:
        x,y,thr = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #범위안에 있으며 지나지않은 알파벳일 경우
            if 0<= nx < R and 0 <= ny < C and graph[nx][ny] not in thr:
                #지나온 알파벳 더해서 queue에 input
                queue.append([nx,ny,thr+graph[nx][ny]])
                #thr은 현재 알파벳 포함X 따라서 +1,최댓값일경우 갱신
                cnt=max(cnt,len(thr)+1)
dx = [1,-1,0,0]
dy = [0,0,1,-1]
bfs(0,0)
print(cnt)
