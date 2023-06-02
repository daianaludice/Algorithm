#https://school.programmers.co.kr/learn/courses/30/lessons/42577
def solution(phoneBook):
    phoneBook.sort()
    for i in range(len(phoneBook)-1):
        if phoneBook[i] == (phoneBook[i+1])[:len(phoneBook[i])]:
            return False
    return True
        
