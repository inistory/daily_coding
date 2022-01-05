def split_to_uv(p):
    stack = []
    left = 0
    right = 0
    correct = True #올바른 괄호 문자열인지 검사
    
    for i,pp in enumerate(p):
        if pp == '(':
            left+=1
            stack.append('(')
        else:
            right+=1
            if len(stack) == 0: #스택이 비어있으면, 올바르지 않은 괄호 문자열
                correct = False
            else: #올바른 괄호 문자열이면
                stack.pop()
        if left == right: #균형잡힌 문자열이 완성되는 순간
            return i+1, correct #v의 시작 인덱스, u의 올바른괄호문자열여부 전달
                

def solution(p):
    #1
    if len(p) == 0:
        return p
    #2
    v_idx, u_correct = split_to_uv(p)
    u = p[:v_idx]
    v = p[v_idx:]
    #3
    if u_correct == True:
        #3-1
        return u + solution(v)
    #4
    else: 
        #4-1, 4-2, 4-3
        answer = '(' + solution(v) + ')'
        #4-4
        for i in range(1,len(u)-1):
            if u[i] == '(':
                answer+=')'
            else:
                answer+='('
        #4-5
        return answer
    
    
    
    