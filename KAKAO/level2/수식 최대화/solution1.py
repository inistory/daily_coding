import re
from itertools import permutations

def solution(expression):
    operator = [x for x in ['*','+','-'] if x in expression]
    operators = [list(y) for y in permutations(operator)]
    #대괄호는 or로인식, 소괄호는 and로 인식 
    expression = re.split(r'(\D)',expression) #(\D)는 숫자가 아닌것 기준으로 split
    
    answer = []
    for operator in operators:
        ex_copy = expression[:] #복사
        for op in operator:
            while op in ex_copy: #부호가 존재하는 동안 반복
                i = ex_copy.index(op) #연산자가 존재하는 곳의 인덱스
                #연산자 바로 전 자리에 계산한 결과를 저장
                ex_copy[i-1] = str(eval(ex_copy[i-1] + ex_copy[i] + ex_copy[i+1]))
                ex_copy = ex_copy[:i] + ex_copy[i+2:] #이미 계산한 부분 제거

        answer.append(ex_copy[0])

    return max(abs(int(x)) for x in answer)