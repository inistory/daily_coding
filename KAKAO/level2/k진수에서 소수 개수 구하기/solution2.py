import math
def trans(n, num): 
    arr = "0123456789ABCDEF" 
    ret = '' 
    if num == 0: 
        return '0' 
    while num > 0: 
        ret = arr[num % n] + ret 
        num = num // n 
    return ret

def solution(n, k):
    n = trans(k,n)
    count = 0
    flag = True
    for num in n.split('0'):
        if num != '' and num != '1':
            num = int(num)
            for i in range(2,int(math.sqrt(num))+1):
                if num % i == 0:
                    flag = False
                    break
            if flag:
                count +=1
    return count