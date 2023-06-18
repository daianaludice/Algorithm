#https://school.programmers.co.kr/learn/courses/30/lessons/42587
from collections import deque

def solution(priorities, location):
    printer = deque((v,i) for i,v in enumerate(priorities))
    count = 0
    while len(printer):
        out = printer.popleft()
        if printer and max(printer)[0] > out[0]:
            printer.append(out)
        else :
            count +=1
            if out[1] == location:
                break
    return count
