#1은 이동할 수 있는 칸
#0은 이동할 수 없는 칸
#(1,1)에서 출발해서 (n,m)위치로 이동할 수 있는 최대 칸 수

from collections import deque
def bfs(i,j):
    q = deque()
    q.append((i,j))
    visited[i][j] = 1

    while q:
        x,y = q.popleft()
        
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]

            if 0<=nx<n and 0<=ny<m and miro[nx][ny]!='0' and not visited[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny] = visited[x][y]+1 #visited에서 갱신

    return visited[n-1][m-1]


n,m = map(int,input().split())
miro = [list(input()) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
answer = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

#미로의 거리 문제와 달리 출발점이 정해져있으므로 for문으로 시작점을 찾은 후 bfs수행하지 않아도됨
print(bfs(0,0))


