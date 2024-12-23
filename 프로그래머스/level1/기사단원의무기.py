def solution(number, limit, power):
    divisors = [0] * (number + 1)
    
    # 약수 개수 구하기 (1부터 number까지)
    for i in range(1, number + 1):
        for j in range(i, number + 1, i):
            divisors[j] += 1
    
    total_weight = 0
    for i in range(1, number + 1):
        if divisors[i] > limit:
            total_weight += power
        else:
            total_weight += divisors[i]
    
    return total_weight
