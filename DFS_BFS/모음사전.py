#https://school.programmers.co.kr/learn/courses/30/lessons/84512
from itertools import product

def solution(word):
    answer = []
    for i in range(1, 6):
        for j in product(['A', 'E', 'I', 'O', 'U'], repeat=i):
            answer.append(''.join(list(j)))
    return sorted(answer).index(word)+1
