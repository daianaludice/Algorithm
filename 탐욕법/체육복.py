#https://school.programmers.co.kr/learn/courses/30/lessons/42862
def solution(n, lost, reserve):
    rlost = [a for a in lost if a not in reserve]
    rreserve = [b for b in reserve if b not in lost]
    rlost.sort()
    rreserve.sort()
    answer = 0
    
    #if len(rreserve) == 0:
    #    return answer
        
    for i in rlost:
        if i-1 in rreserve:
            answer +=1
            rreserve.remove(i-1)
        elif i+1 in rreserve:
            answer +=1
            rreserve.remove(i+1)
    return n-len(rlost)+answer
