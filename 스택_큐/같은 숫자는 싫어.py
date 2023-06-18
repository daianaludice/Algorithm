#https://school.programmers.co.kr/learn/courses/30/lessons/12906
def solution(arr):
    answer = []
    result = arr[0]
    for a in arr[1:]:
        if result != a:
            answer.append(result)
            result = a
        else:
            continue
    answer.append(arr[-1])
    return answer
