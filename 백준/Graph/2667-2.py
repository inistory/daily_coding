from collections import deque

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1
    count = 1
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    while queue:
        x,y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if 0<=nx<n and 0<=ny<n and graph[nx][ny]=='1' and not visited[nx][ny]:
                queue.append((nx,ny))
                visited[nx][ny] = 1
                count+=1
    return count

n = int(input())
graph = [input() for _ in range(n)]
visited = [[0]*n for _ in range(n)]
answer = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == '1' and not visited[i][j]:
            answer.append(bfs(i,j))
            
print(len(answer))
answer.sort()
for a in answer:
    print(a)