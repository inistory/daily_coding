def solution(n):
    if int(n**(1/2))==n**(1/2): #정수인지 확인하는 방법
        return (n**(1/2)+1)**2
    else:
        return -1