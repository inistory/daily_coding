import math
def convert(n, base):#n:10진수 base: 진수 k
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]

def solution(n, k):
    n = convert(n,k)
    count = 0
    check = True
    for num in n.split('0'):
        if num != '' and num != '1': #빈값이 아니고 1이 아닐 때
            num = int(num)
            #소수인지 검사
            for i in range(2,int(math.sqrt(num))+1):
                if num % i == 0: #나누어떨어지는 수가 있으면
                    check = False #소수가 아님
                    break
            if check: #check가 True라면
                count +=1 #소수니까 +1
    return count