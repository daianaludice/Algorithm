#https://www.acmicpc.net/problem/16927
# 20230527 문제 : 배열 돌리기 2 / 알고리즘 : 구현
# get 함수는 일자로 해당 부분을 리스트화하는 함수
def get(k,n,m,board):
    # -2는 모서리부분을 제외 -2*2 임으로 가로세로 중복제거됨
    #겉부분을 계속 돌아야함으로 겉부분의 총길이는 (n+m-2)*2
    C = [0]*((n+m-2)*2)
    # 0,0 과 같은 시작위치
    i,j,t = k,k,0
    for _ in range(n-1):
        C[t] = board[i][j]
        i += 1
        t +=1
    for _ in range(m-1):
        C[t] = board[i][j]
        j +=1
        t += 1
    for _ in range(n-1):
        C[t] = board[i][j]
        i -=1
        t += 1
    for _ in range(m-1):
        C[t] = board[i][j]
        j -=1
        t += 1
    return C

# put 함수는 get함수의 반대
def put(C,k,n,m,board):
    i,j,t = k,k,0
    for _ in range(n-1):
        board[i][j] = C[t]
        i += 1
        t += 1
    for _ in range(m-1):
        board[i][j] = C[t]
        j +=1
        t += 1
    for _ in range(n-1):
        board[i][j] = C[t]
        i -=1
        t += 1
    for _ in range(m-1):
        board[i][j] = C[t]
        j -=1
        t += 1
    return C

#회전시키는 함수
def rotate(k,n,m,r,board):
    chain = get(k,n,m,board)
    #잘라야하는 위치는 일자로된 리스트에 돌려야하는 값 k 으로 자른것
    idx = len(chain) - (r % len(chain))
    #잘라서 붙임
    rotated = chain[idx:] + chain[:idx]
    #자른값 다시 넣기
    put(rotated,k,n,m,board)


N,M,R = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
#회전되는 판의 수, 만들어야하는 체인의 수
num = min(N,M)//2

for k in range(num):
    #회전하는 판이 작아지면 작아질때마다 양끝부분을 빼야함으로 가로,세로 각각 -2씩 되어 반복
    rotate(k, N - 2 * k, M - 2 * k, R, board)
for i in range(N):
    print(" ".join(map(str, board[i])))
