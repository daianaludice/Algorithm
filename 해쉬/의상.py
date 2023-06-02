#https://school.programmers.co.kr/learn/courses/30/lessons/42578
def solution(clothes):
    answer = 1
    dic = {}
    for j in clothes:
        dic[j[1]]= [] 
    for item ,key in clothes:
        dic[key].append(item)
    for i in dic.values():
        answer *= len(i)+1
    return answer-1
