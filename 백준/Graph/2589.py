#보물섬
from collections import deque
L, W = map(int, input().split())
map = [list(map(str, input())) for _ in range(L)]
queue = deque()

dx = [1,-1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue.append((x,y))
    visited = [[0]*W for i in range(L)]
    visited[x][y] = 1
    num = 0
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            
            if 0<=nx<L and 0<=ny<W and not visited[nx][ny] and map[nx][ny] == 'L':
                visited[nx][ny] = visited[x][y]+1 #방문했던걸 더 방문하기 위해서
                num = max(num, visited[nx][ny])
                queue.append((nx,ny)) 
                
    return num-1
                    
cnt = 0                
for i in range(L):
    for j in range(W):
        if map[i][j] == 'L': #육지를 만나면 탐색         
            cnt = max(cnt,bfs(i,j))
            
print(cnt)