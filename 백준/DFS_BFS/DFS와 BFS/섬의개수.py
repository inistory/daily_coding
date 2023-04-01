from collections import deque
def bfs(i,j,w,h):
    q = deque()
    q.append((i,j))
    island[i][j] = 2
    
    while q:
        x,y = q.popleft()

        for k in range(8):
            nx = x+dx[k]
            ny = y+dy[k]

            if 0<=nx<h and 0<=ny<w and island[nx][ny]==1:
                island[nx][ny] = 2
                q.append((nx,ny))      

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    island = [list(map(int, input().split())) for _ in range(h)]
    answer = 0
    dx = [0,0,-1,1,-1,-1,1,1]
    dy = [-1,1,0,0,1,-1,1,-1]
    for i in range(h):
        for j in range(w):
            if island[i][j] == 1:
                bfs(i,j,w,h)
                answer+=1
    print(answer)