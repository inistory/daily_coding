from collections import deque

def solution(maps):
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    m = len(maps)
    n = len(maps[0])
    visited = [[0]*n for _ in range(m)]
    
    queue = deque()
    queue.append((0,0,1))
    visited[0][0] = 1

    while queue:
        x,y,count = queue.popleft()
        if x== m-1 and y == n-1:
            return count
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<m and 0<=ny<n and not visited[nx][ny]:
                if maps[nx][ny] == 1:
                    visited[nx][ny]=1
                    queue.append((nx,ny,count+1))
    return -1