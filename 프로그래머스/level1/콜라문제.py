def solution(a, b, n):
    #a개를 가져다주면 b개를 받는다
    #가지고 있는 빈병의 개수 n개
    total = 0 #받을수 있는 콜라의 수
    new_cola = 0
    
    while n >=a:
        new_cola = (n//a)*b
        total +=new_cola
        n = n%a + new_cola
    
    return total
    