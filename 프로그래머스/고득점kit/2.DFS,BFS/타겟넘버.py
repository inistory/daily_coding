from collections import deque
    
def solution(numbers, target):
    answer = 0
    q = deque()
    q.append((numbers[0]*1,0))
    q.append((numbers[0]*(-1),0))
    
    while q:
        ca, ci = q.popleft() #연산결과, 인덱스
        ci+=1
        if ci >= len(numbers):
            if ca == target:
                answer+=1
        else:
            q.append((ca+numbers[ci],ci))
            q.append((ca-numbers[ci],ci))
    
    return answer
                
    