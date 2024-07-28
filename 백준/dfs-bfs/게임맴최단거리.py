from collections import deque

def solution(maps):
    r = len(maps)
    c = len(maps[0])
    
    def bfs(i,j):
        q = deque()
        q.append((i,j))
        visited[i][j] = 1
        
        while q:
            x,y = q.popleft()

            for k in range(4):
                nx = x+dx[k]
                ny = y+dy[k]

                if 0<=nx<r and 0<=ny<c and maps[nx][ny]!=0:
                    if visited[nx][ny] == -1:              
                        q.append((nx,ny))
                        visited[nx][ny] = visited[x][y]+1

        return visited[-1][-1]

    answer = 0
    visited = [[-1]*c for i in range(r)]
    
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    
    answer = bfs(0,0)
    return answer
            