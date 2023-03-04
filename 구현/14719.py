#구현문제 https://www.acmicpc.net/problem/14719
#문제 : 빗물
import sys
input = sys.stdin.readline


H,W = map(int,input().split())
block = list(map(int,input().split()))
result = 0

for i in range(1,W-1):
    #i를 기준으로 왼쪽 오른쪽 확인, i의 높이보다 높아야 i가 고일수있다.
    left = max(block[:i])
    right = max(block[i+1:])
    #최대 올라갈수 있는 수면높이 low
    low = min(left,right)
    #물이 고일 수 있는지 확인
    if block[i] < low:
        #누적 합계
        result += low-block[i]
print(result)
