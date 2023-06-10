#https://school.programmers.co.kr/learn/courses/30/lessons/42839
import math
from itertools import permutations

def is_prime(x):
    if x == 0 or x== 1:
        return False
    for i in range(2,int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True
def solution(numbers):
    answer = 0
    s = set()
    number = list(i for i in numbers)
    for i in range(1,len(numbers)+1):
        num = list(permutations(number, i))
        for n in num:
            s.add(int(''.join(n)))
    for j in s:
        if is_prime(j):
            answer +=1
    return answer
