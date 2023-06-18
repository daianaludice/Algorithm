#https://www.acmicpc.net/problem/2799
M,N = map(int,input().split())

none = ["....","....","....","...."]
one = ["****","....","....","...."]
two = ["****","****","....","...."]
three = ["****","****","****","...."]
four = ["****","****","****","****"]

graph = []
while len(graph)!= 5*M+1:
    graph.append(input())

r,c = [],[]
for m in range(M):
    r.append(5*m+1)
for n in range(N):
    c.append(5*n+1)

answer = []
for i in r:
    for j in c:
        result = []
        result.append(graph[i][j:j+4])
        result.append(graph[i+1][j:j+4])
        result.append(graph[i+2][j:j+4])
        result.append(graph[i+3][j:j+4])
        answer.append(result)

print(answer.count(none),answer.count(one),answer.count(two),answer.count(three),answer.count(four))
