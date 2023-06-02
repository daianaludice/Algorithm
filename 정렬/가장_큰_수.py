#https://school.programmers.co.kr/learn/courses/30/lessons/42746
def solution(numbers):
    if sum(numbers) == 0:
        return "0"
    number = list(str(i)*3 for i in numbers)
    number.sort(reverse=True)
    return ''.join(map(lambda x:x[:len(x)/3],number))
