#유클리드호제법참고
def gcd(a,b):
    while b!=0:
        a,b = b, a%b
    return a
    
def solution(n, m):
    gcd_value = gcd(n,m)
    lcm_value = (n*m) // gcd_value
    return [gcd_value,lcm_value]

#math활용
import math

def solution(n, m):
    # 최대공약수 계산
    gcd = math.gcd(n, m)
    # 최소공배수 계산
    lcm = (n * m) // gcd
    # 결과 반환
    return [gcd, lcm]
