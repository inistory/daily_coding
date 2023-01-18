#시간초과 코드
def solution(gems):
    n = len(gems)
    min_len = len(set(gems))
    test_length = [i for i in range(min_len,n)]
    for length in test_length:
        for i in range(0, n):
            target = gems[i:i+length]
            if len(target) == length:
                if len(set(target)) == min_len:
                    return [i+1,i+length]
            
    return [1,n]