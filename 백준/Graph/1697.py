#숨바꼭질
from collections import deque
import sys

MAX_POS = 100000
input = sys.stdin.readline
visited = [0] * (MAX_POS+1)

def bfs(N):
    queue = deque()
    queue.append((N, 0))
    visited[N] = 1
    
    while queue:
        x, cnt = queue.popleft()
        if x == K:
            return cnt
        
        for i in (x-1,x+1,x*2):
            if 0<=i<=MAX_POS and not visited[i]:
                queue.append((i,cnt+1))
                visited[i] = 1

N, K = map(int, input().split())
print(bfs(N))
    
    
    
