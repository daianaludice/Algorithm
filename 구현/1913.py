#https://www.acmicpc.net/problem/1913
N = int(input())
M = int(input())

graph = [[0 for _ in range(N)] for _ in range(N)]
#바깥에서 안쪽으로 이동
move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

num = N**2
x,y = 0,0
curve = 0
while num > 0:
    graph[y][x] = num
    ny, nx = move[curve]
    dx = x + nx
    dy = y + ny
    #갈수없거나 방문한 곳
    if 0 > dx or dx >= N or 0 > dy or dy >= N or graph[dy][dx] != 0:  
        curve = (curve + 1) % 4

    ny, nx = move[curve]
    x += nx
    y += ny
    num -= 1

#graph출력 및 M의위치 찾기
temp_x, temp_y = 0, 0
for i in range(N):
    for j in range(N):
        if graph[i][j] == M:
            temp_x = j
            temp_y = i
        print(graph[i][j], end=" ")
    print()
print(temp_y + 1, temp_x + 1)
