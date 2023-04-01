from collections import deque

def bfs(i,j,idx):
    
    q = deque()
    q.append((i,j,idx))#큐에 넣기
    visited[i][j] = 1 #방문처리

    
    #조건을 만족하면 큐에 넣기
    while q: #큐가 비어있지 않을때
        x,y,cnt = q.popleft()  #꺼내기
        if m[x][y] == '3':
            return cnt-1#종료조건을 만족하면 return
        #해당 좌표의 상하좌우 살피기
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<msize and 0<=ny<msize and m[nx][ny]!='1' and not visited[nx][ny]:
                q.append((nx,ny,cnt+1)) 
                visited[nx][ny] = 1
    return 0


T = int(input())
idx =0 #몇번이동했는지
answer = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]
answer = 0
for ts in range(1,T+1):
    msize = int(input())
    m = [list(input()) for _ in range(msize)]
    visited = [[0]*msize for _ in range(msize)]

    for i in range(msize):
        for j in range(msize):
            if m[i][j] == '2': #시작지점에서
                answer = bfs(i,j,0)

    print(f'#{ts} {answer}')               