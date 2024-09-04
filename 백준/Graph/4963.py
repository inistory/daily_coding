#섬의 개수
from collections import deque
w, h = 49,49
dx = [0,0,-1,1,-1,-1,1,1]
dy = [-1,1,0,0,1,-1,1,-1]


def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1
    
    while queue:
        x,y = queue.popleft()
    
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<h and 0<=ny<w and graph[nx][ny]==1 and not visited[nx][ny]:
                visited[nx][ny] = 1
                queue.append((nx,ny))
            
while w!=0 and h!=0:
    w, h = map(int, input().split())
    if w==0 and h==0:
        break
    graph = [list(map(int,input().split())) for _ in range(h)]
    visited = [[0]*w for _ in range(h)]
    count = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and not visited[i][j]:
                bfs(i,j)
                count+=1
                
    print(count)
