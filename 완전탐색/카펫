#https://school.programmers.co.kr/learn/courses/30/lessons/42842
def solution(brown, yellow):
    num = brown + yellow
    for n in range(1, num+1):
        if num%n != 0:
            continue
        m = num//n
        if (n-2)*(m-2) == yellow:
            return sorted([n, m], reverse = True)
