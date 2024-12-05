def solution(num):
    count = 0
    while num!=1:
        if num%2==0:
            num=num/2
            count+=1
        elif num%2!=0:
            num=num*3+1
            count+=1
        
        if count == 500 and num!=1:
            return -1
        if num == 1:
            return count
    
    return count