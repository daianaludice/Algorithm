#https://school.programmers.co.kr/learn/courses/30/lessons/87946
from itertools import permutations
def solution(k, dungeons):
    num = [i for i in range(len(dungeons))]
    order = list(permutations(num, len(dungeons)))
    print(num,order)
    count = 0
    for each_order in order:
        hp = k
        each_count = 0
        for i in each_order:
            if hp >= dungeons[i][0]:
                hp -= dungeons[i][1]
                each_count += 1
            else:
                break
        count = max(count, each_count)

    return count
