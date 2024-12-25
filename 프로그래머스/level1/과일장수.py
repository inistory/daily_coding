def solution(k, m, score):
    score.sort(reverse=True)
    answer = 0
    for i in range(0,len(score),m):
        if i+m <= len(score):
            answer+=min(score[i:i+m])*m
    return answer