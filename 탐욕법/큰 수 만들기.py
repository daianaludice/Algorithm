#https://school.programmers.co.kr/learn/courses/30/lessons/42883
def solution(number, k):
    #answer를 스택으로 사용
    answer = []
    for i in number:
        #return할 숫자가 정해진게 없으면 그냥 하나 push
        if len(answer) == 0:
            answer.append(i)
            continue
        #제거할 숫자가 더 있으면 진행
        if k > 0:
            #맨뒤에자리를 다음에 넣을 수와 비교
            while answer[-1] < i:
                #i를 넣어야되니 있던거 버림
                answer.pop()
                #for문 마지막에 push할거니 미리빼기
                k -= 1
                #맨 앞이거나 맨 뒤면 while문X,break
                if len(answer) == 0 or k <= 0:
                    break
        #맞는 수 집어넣기
        answer.append(i)
    #만일 number가 한숫자로만 이루어질경우 예외처리하여 출력
    return ''.join(answer[:len(answer) - k])
