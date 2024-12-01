def solution(t, p):
    #p길이만큼 부분수열 생성, 이들 중에 p보다 작은 수의 개수 return
    count = 0
    for i in range(0,len(t)-len(p)+1):
        s = t[i:i+len(p)]
        
        if int(s) <= int(p):
            count+=1
    
    return count