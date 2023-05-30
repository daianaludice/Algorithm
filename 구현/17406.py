#https://www.acmicpc.net/problem/17406
# 230530 문제: 배열 돌리기 4 알고리즘 : 구현,브루드포스
# 10:36 ~ 12:08
from itertools import *
import copy
N,M,K = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
operation = [list(map(int,input().split())) for _ in range(K)]
#모든 임의의 순서 리스트
opers = list(permutations(operation,K))
cnt = int(1e9)

def get(graph,n,m,r,c,k):
    C = [0] * ((n + m - 2) * 2)
    i,j,t =r+k,c+k,0
    for _ in range(n-1):
        C[t] = graph[i][j]
        i += 1
        t +=1
    for _ in range(m-1):
        C[t] = graph[i][j]
        j +=1
        t += 1
    for _ in range(n-1):
        C[t] = graph[i][j]
        i -=1
        t += 1
    for _ in range(m-1):
        C[t] = graph[i][j]
        j -=1
        t += 1
    return C

# put 함수는 get함수의 반대
def put(C, graph, n, m,r,c,k):
    i,j,t = r+k,c+k,0
    for _ in range(n-1):
        graph[i][j] = C[t]
        i += 1
        t += 1
    for _ in range(m-1):
        graph[i][j] = C[t]
        j +=1
        t += 1
    for _ in range(n-1):
        graph[i][j] = C[t]
        i -=1
        t += 1
    for _ in range(m-1):
        graph[i][j] = C[t]
        j -=1
        t += 1
    return graph

def rotate(graph,n,m,r,c,k):
    chain = get(graph,n,m,r,c,k)
    # -1하여 한 칸 회전
    rotated = chain[1:] + chain[:1]
    put(rotated, graph, n, m,r,c,k)


for oper in opers:
    graph = copy.deepcopy(board)
    #각 경우에 따라 회전시키기
    for r,c,s in oper:
        #회전할 판의 크기 구하기
        n = (r+s)-(r-s)+1
        m = (c+s)-(c-s)+1
        #회전할 판의 시작 위치
        i = (r-s)-1
        j = (c-s)-1
        #만들어야하는 체인의 수
        num = min(n, m) // 2
        for k in range(num):
            # 회전하는 판이 작아지면 작아질때마다 양끝부분을 빼야함으로 가로,세로 각각 -2씩 되어 반복
            rotate(graph, n- 2 * k , m - 2 * k,i,j,k)
    #회전된 판의 각 행의 값 중 최소값으로 갱신
    for n in range(N):
        cnt = min(cnt,sum(graph[n]))
print(cnt)
