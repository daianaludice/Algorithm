#https://school.programmers.co.kr/learn/courses/30/lessons/1844
from collections import deque

def bfs(maps,x, y):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        queue = deque()
        queue.append((x, y))
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]): 
                    continue
                if maps[nx][ny] == 0:  
                    continue
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))
        return maps[len(maps)-1][len(maps[0])-1]
    
def solution(maps):
    answer = bfs(maps,0, 0)
    return -1 if answer == 1 else answer
