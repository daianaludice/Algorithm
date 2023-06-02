#https://school.programmers.co.kr/learn/courses/30/lessons/42576
from collections import Counter

def solution(participant, completion):
    answer = Counter(participant)-Counter(completion)
    #answer = [x for x in participant if x not in completion]
    return (','.join(answer))
