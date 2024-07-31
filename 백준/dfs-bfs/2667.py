#단지번호붙이기
from collections import deque

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    visited[x][y] = 1

    count = 1
    while queue:
        x,y = queue.popleft()
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0<=nx<n and 0<=ny<n and map[nx][ny] == '1' and not visited[nx][ny]:
                queue.append((nx,ny))
                visited[nx][ny] = 1
                count+=1
    return count
        
n = int(input()) #단지갯수
map = [input() for _ in range(n)]
visited = [[0] * n for _ in range(n)]
home_info = []

for i in range(n):
    for j in range(n):
        if map[i][j] == '1' and not visited[i][j]:
            home_info.append(bfs(i,j))

home_info.sort()
print(len(home_info))
for h in home_info:
    print(h)            
