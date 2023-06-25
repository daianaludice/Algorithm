#https://www.acmicpc.net/problem/1976
N = int(input())
M = int(input())
#부모노드는 자기자신으로 초기화 0은제외


#두 집합이 다르면 합치기
def union(i,j):
    i = find(i)
    j = find(j)
    if i==j:
        return
    else:
        parent[j]=i
        return parent[j]
    
#부모노드찾기    
def find(x):
    if parent[x] ==x:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]
    
#0부터 n까지 부모노드 자기자신으로 초기화
parent = [n for n in range(N+1)]    
for i in range(1,N+1):
    graph = list(map(int,input().split()))
    for j in range(1,N+1):
        if graph[j-1] == 1:
            union(i,j)
#여행경로            
path = list(map(int,input().split()))
#set으로 묶인 집합들 구하기
result =set([find(i) for i in path])
#묶인 집합이 1개, 모두 한 집합이면 YES            
print('YES' if len(result)==1 else 'NO')
