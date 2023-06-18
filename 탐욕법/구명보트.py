#https://school.programmers.co.kr/learn/courses/30/lessons/42885
from collections import deque

def solution(people, limit):
    answer = 0
    #무거운거 먼저 앞으로 오도록
    people.sort(reverse = True)
    #큐
    queue = deque(people)
    while queue:
        #맨앞에꺼 보트 태우고 남은무게
        result = limit - queue.popleft()
        #남은 무게가 제일 가벼운거를 태워도 남거나 딱맞으면
        while queue and queue[-1] <= result:
            #2명이상태울수있게 빼주고 다시 while문 불가능하면 그대로 카운팅
            result -= queue.pop()
        answer += 1
    return answer
