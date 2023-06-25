#https://www.acmicpc.net/problem/2512
n =int(input())
region = list(map(int,input().split()))
budget = int(input())
sum_result = sum(region)
if sum_result <= budget:
    print(max(region))
else:
    answer =0
    region = sorted(region)
    i,k = 1,region[-1]
    j = int((i+k)/2)
    if region[0] == region[-1] and (region[0]-1)*len(region) <= budget:
        answer = region[0]-1
    else:
        while 1 :
            if k <= i:
                break
            result,count = 0,0
            for a in region:
                if a <= j:
                    result += a
                    count += 1
                    continue
                else:
                    break
            result += (len(region)-count)*j
            if result > budget:
                k = j
                j =(i+k)/2
            elif result < budget:
                answer = j
                i = j
                j = (i+k)/2
            else:
                answer =j
                break
    print(int(answer))
