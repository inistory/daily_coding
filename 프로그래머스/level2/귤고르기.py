# https://school.programmers.co.kr/learn/courses/30/lessons/138476
def solution(k, tangerine):
    answer = 0
    guel = {}
    for i,g in enumerate(tangerine):
        if g not in guel:
            guel[g] = 1
        else:
            guel[g] += 1
            
    sorted_guel = sorted(guel.items(), key=lambda x: x[1], reverse=True)   

    for key, value in sorted_guel:
        k = k - value
        answer += 1
        if k <= 0:
            break 
    
    return answer