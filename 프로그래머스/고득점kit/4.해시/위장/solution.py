def solution(clothes):
    answer = {}
    cnt = 1
    for cloth in clothes:
        if cloth[1] in answer: 
            answer[cloth[1]] += 1
        else: 
            answer[cloth[1]] = 1

    for i in answer.values():
        cnt *= (i+1) #각 카테고리별로 장착하지 않은 경우의 수를 포함하면 +1
    return cnt - 1 #아무것도 장착하지 않은 경우 빼기