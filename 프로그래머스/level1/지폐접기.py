def check(wallet, cur_bill):
    #크고 작은걸 찾고 매칭해서 확인
    w_a, w_b = (wallet[0], wallet[1]) if wallet[0] > wallet[1] else (wallet[1], wallet[0])
    c_a, c_b = (cur_bill[0], cur_bill[1]) if cur_bill[0] > cur_bill[1] else (cur_bill[1], cur_bill[0])
    
    if w_a >=c_a and w_b>=c_b:
        return True
    else:
        return False

def solution(wallet, cur_bill):
    count = 0
    
    while not check(wallet, cur_bill): #지갑에 넣을 수 없을 때 반복
        #더 큰 값을 찾고 그걸 반띵해
        a, b = cur_bill[0], cur_bill[1]
        if a > b:
            a = a//2
            cur_bill = [a,b]
            print(cur_bill)
            count+=1
        else:
            b = b//2
            cur_bill = [a,b]
            print(cur_bill)
            count+=1
    
    return count
        
    