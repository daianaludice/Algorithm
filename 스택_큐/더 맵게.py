#https://school.programmers.co.kr/learn/courses/30/lessons/42626
import heapq

def solution(scoville, K):
    answer = 0
    scoville.sort()
    while scoville[0] < K:
        if len(scoville) <= 1:
            return -1
        else:
            s = heapq.heappop(scoville)
            s2 = heapq.heappop(scoville)
            heapq.heappush(scoville, (s + (s2 * 2)))
            answer += 1
    return answer
