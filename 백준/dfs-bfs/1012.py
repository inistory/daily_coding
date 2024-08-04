#유기농 배추
from collections import deque
test_case = int(input())

def bfs(x,y):
    count = 0
    queue = deque()
    queue.append((x,y))
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    while queue:
        x,y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<M and 0<=ny<N and not visited[nx][ny] and bat[nx][ny] == 1:
                visited[nx][ny] = 1
                queue.append((nx,ny))
            

for t in range(test_case):
    M,N,K = map(int, input().split()) #가로, 세로, 배추개수
    bat = [[0]*(N+1) for _ in range(M+1)]
    visited = [[0]*(N+1) for _ in range(M+1)]
    for _ in range(K):
        u,v = map(int, input().split())
        bat[u][v] = 1
    count = 0
    for m in range(M):
        for n in range(N):
            if not visited[m][n] and bat[m][n] == 1:
                bfs(m,n)
                count+=1
    print(count)

    