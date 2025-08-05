from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
papers = list(map(int, input().split()))
dq = deque((i+1, papers[i]) for i in range(N)) #풍선번호 이동값
result = []

while dq:
    idx, move = dq.popleft()
    result.append(idx)
    
    if move > 0:#양수면 오른쪽
        dq.rotate(-(move-1))#1을 뺐기때문에 -1해줌
    else:#음수면 왼쪽
        dq.rotate(-move)#1없앴으니까 바로 왼쪽으로 이동 가능
        
print(' '.join(map(str, result)))