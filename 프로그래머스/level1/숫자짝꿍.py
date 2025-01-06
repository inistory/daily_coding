from collections import Counter
def solution(X, Y):
    #두 정수에서 공통으로 나타나는 정수
    #그 수들로 제일큰 정수만들기
    count_X = Counter(X)
    count_Y = Counter(Y)  
    answer = ''
    for i in range(10):
        count = min(count_X[str(i)],count_Y[str(i)])
        answer+= str(i)*count
    
    if answer == '':
        return "-1"
    if all(a == "0" for a in answer):
        return "0"
    
    answer = sorted(answer,reverse=True)
    return ''.join(answer)