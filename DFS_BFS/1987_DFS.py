import sys

input = sys.stdin.readline
R,C = map(int,input().split())
graph = [list(input()) for _ in range(R)]
#출발점부터 카운트
cnt = 1

    
def dfs(x,y,thr):
    global cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        #범위안에 있으며 지나지않은 알파벳일 경우
        if 0<= nx < R and 0 <= ny < C and graph[nx][ny] not in thr:
            #지나온 알파벳 더해서 재귀
            dfs(nx,ny,thr+graph[nx][ny])
            #thr은 현재 알파벳 포함X 따라서 +1,최댓값일경우 갱신
            cnt=max(cnt,len(thr)+1)
dx = [1,-1,0,0]
dy = [0,0,1,-1]
dfs(0,0,graph[0][0])
print(cnt)
