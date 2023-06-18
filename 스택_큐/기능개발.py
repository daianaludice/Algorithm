#https://school.programmers.co.kr/learn/courses/30/lessons/42586
from collections import deque
import math

def solution(progresses, speeds):
    workday =[math.ceil((100-i)/j)for i,j in zip(progresses, speeds)]
    work = deque(workday)
    count=1
    answer = []
    while(work):
        if count > 1 :
            count-=1 
            prog=work.popleft()
            continue
        prog=work.popleft()
        for progres in work : 
            if prog >= progres :
                count+=1 
            else :
                break
        answer.append(count)
    return answer
