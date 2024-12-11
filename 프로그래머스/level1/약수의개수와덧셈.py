def factor_check(i):
    #개수가 홀수면 True
    
    #개수가 짝수면 False
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    
    if count%2==0:
        return False
    else:
        return True
            

def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if factor_check(i):
            answer-=i
        else:
            answer+=i
    
    return answer