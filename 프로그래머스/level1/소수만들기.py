from itertools import combinations

def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True


def solution(nums):
    #combination해서 더한값이 소수인지 검사
    #소수인지 검사하는 함수
    answer = 0
    for num in list(combinations(nums,3)):
        if is_prime(sum(num)):
            answer+=1
    
    return answer