#안전 영역
from collections import deque
n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
max_value = max(max(row) for row in graph)

dx = [0,0,-1,1]
dy = [-1,1,0,0]


def bfs(x,y,r):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        visited[x][y] = 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                if graph[nx][ny] > r:
                    visited[nx][ny] = 1
                    queue.append((nx,ny))
        
answer = 0
for r in range(max_value+1):
    visited = [[0]*(n+1) for _ in range(n+1)]
    count = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] >r and not visited[i][j]:
                bfs(i,j,r)
                count+=1
    answer = max(answer, count)
    
print(answer)
                