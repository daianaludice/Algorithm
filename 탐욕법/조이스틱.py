#https://school.programmers.co.kr/learn/courses/30/lessons/42860
def solution(name):
    answer = 0
    #전부 A이면 0
    if set(name) == {'A'}:
        return 0
    #name은 아스키코드값으로 변경
    name = [ord(j) for j in list(name)]
    #a와의 거리값 위/아래움직여야하는 위치값 저장
    result = [i-65 if i <= 78 else 91-i for i in list(name)]
    answer += sum(result)
    #그냥 쭉가는 경우,즉 최대이동거리
    default = len(result)-1
    #A가없으면 그냥쭉감
    if 65 not in name:    
        answer += default
        return answer
    #result_list = [i for i, value in enumerate(name) if value == 65]
    #i는위치,c는name의값
    for i, c in enumerate(name):
        #연속된 A찾기
        num = i + 1
        #맨끝이아니고 A일경우
        while num < len(name) and name[num] == 65:
            #카운팅
            num += 1            
        # 그냥 최대거리,왼쪽갔다가 오른쪽으로 갈 경우, 오른쪽갔다 왼쪽으로 갈 경우
        LR = 2 *i + len(name) - num
        RL = i + 2 * (len(name) -num)
        default = min(default,LR,RL)
    answer += default
    return answer
