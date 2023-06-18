#https://school.programmers.co.kr/learn/courses/30/lessons/12909
def solution(s):
    if (s.count('(')) != s.count(')'):
        return False
    count = 0
    for i in list(s):
        if i == '(':
            count += 1
        else:
            count -= 1
        if count <0:
            return False  
    return True
