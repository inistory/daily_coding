def solution(total, budget):
    answer = 0
    count = 0
    total.sort()
    for t in total:
        if budget - t >=0:
            budget-=t
            count+=1
    
    return count