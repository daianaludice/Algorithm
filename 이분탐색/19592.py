#https://www.acmicpc.net/problem/19592
T= int(input())
for i in range(T):
    #N는 참가자 수, X는 트랙길이 V는 부스터최대속력
    N,X,V = map(int,input().split()) 
    n =list(map(int,input().split()))
    #부스터가 아닌 내속력
    z = n[-1]
    #제일 빠른사람 속력
    fast = max(n[:N-1])
    #제일 빠른사람이 걸린시간
    c = float(X/fast)
    #부스터없이 내가 더 빠르면 0
    if z > fast:
        print(0)
    #부스터를 써서 이길수있다면
    else:
        i,j =0,V
        while 1:
            #이분탐색
            v = (i+j)//2
            #부스터를 써서 들어가는데 걸린시간
            boost = ((X-v)/z)+1
            #범위를 벗어나면 break
            if i > j:
                break
            #제일 빠른 사람보다 더 오래걸렸으면 최소치 증가
            elif boost >= c:
                i = v+1
            #반대면 최대값 감소
            else:
                j = v-1
        #이길수있는 부스터값이 최댓값을 넘어가면-1
        if i > V:
            print(-1)
        #아니면 출력
        else:
            print(i)
        #booster = (c*fast)-((c-1)*z)
        #print(int(booster+1))
