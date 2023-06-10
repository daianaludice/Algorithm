#https://school.programmers.co.kr/learn/courses/30/lessons/42840
def solution(answers):
    answer = []
    count = [0,0,0]
    s1 = [1,2,3,4,5]
    s2 = [2,1,2,3,2,4,2,5]
    s3 = [3,3,1,1,2,2,4,4,5,5]
    
    for i in range(len(answers)):
        if answers[i] == s1[i%5]:
            count[0] +=1
        if answers[i] == s2[i%8]:
            count[1] +=1
        if answers[i] == s3[i%10]:
            count[2] +=1
    for j,n in enumerate(count):
        if n == max(count):
            answer.append(j+1)
            
    
    return answer
