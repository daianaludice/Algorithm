#https://school.programmers.co.kr/learn/courses/30/lessons/42747
def solution(citations):
    citations.sort(reverse=True)
    for i in range(len(citations)):
        if citations[i] <= i:
            return i
    return len(citations)
