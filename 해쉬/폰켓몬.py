#https://school.programmers.co.kr/learn/courses/30/lessons/1845
def solution(nums):
    num = list(set(nums))
    return min(len(num),len(nums)/2)
