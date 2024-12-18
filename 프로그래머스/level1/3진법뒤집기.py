def solution(n):
    #10진법 -> 3진법
    answer = ''
    a = n
    while a!=0:
        n = a
        a, b = n//3, n%3  #몫, 나머지
        answer+=str(b) 
    return int(answer,3) #3진법->10진법
    
    