#https://school.programmers.co.kr/learn/courses/30/lessons/42584
from collections import deque
def solution(prices):
    answer = []
    queue = deque(prices)
    while(queue):
        price = queue.popleft()
        count = 0
        for next_price in queue:
            count +=1
            if next_price < price:
                break
        answer.append(count)
                
    return answer
