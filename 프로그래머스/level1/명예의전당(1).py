def solution(k, score):
    answer = []
    t = []
    
    for i,s in enumerate(score):
        if i < k:
            answer.append(s)
            answer.sort()
        else:
            if s > answer[0]: #여기에 있는 수 중에 가장 작은 수보다 크면
                answer.append(s)
                answer.remove(answer[0])
                answer.sort()
            
        t.append(answer[0])
    
    return t
    
                
            