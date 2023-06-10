#https://school.programmers.co.kr/learn/courses/30/lessons/43165
from itertools import product

def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s= list(map(sum,product(*l)))
    return s.count(target)
