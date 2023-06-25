#https://www.acmicpc.net/problem/13777
while 1:
    n = int(input())
    #끝나는 지점
    if n == 0:
        break
    #범위값1~50
    x,y = 1, 50
    #범위가 없어지면 끝
    while x <= y:
        #몫으로 값정함,출력을 먼저하고 나중에판별
        m = (x+y)//2
        print(m, end=' ')
        #찾으면 break
        if m == n:
            break
        # 찾아야하는 값이 현재값보다 크면 최소범위값을 현재값+1로 지정 
        elif m < n:
            x = m+1
        # 찾아야하는 값이 현재값보다 작으면 최대범위값을 현재값-1로 지정
        else:
            y = m-1
    #한 숫자가 끝나면 다음줄로넘기기
    print()
