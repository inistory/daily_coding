def fail_percent(target_stage, stages):
    check = 0
    denominator = 0
    count = 0
    for i,number in enumerate(stages):
        if number == target_stage: 
            if check==0:
                denominator = len(stages[i:])
                check+=1
                count+=1
            else:
                count+=1
                
    if denominator !=0:
        return count / denominator
    else:
        return 0

def solution(N, stages):
    answer = []
    stages.sort()
    storage = {}
    for i in range(N):
        storage[i+1] = fail_percent(i+1,stages)
        
    answer = sorted(storage, key= lambda x : storage[x], reverse=True)
    return answer
