#섬 뭉텅이를 찾는 문제
#1이 나올때마다 bfs수행
#방문한 섬은 상태를 2로 바꿔주기
#bfs수행 횟수를 return
#대각선으로 이어져도 하나의 섬인 것을 기억

from collections import deque
def bfs(i,j,w,h):
    q = deque()
    q.append((i,j))
    island[i][j] = 2 #visited가 필요없는 이유, island값을 2로 변경
    
    while q:
        x,y = q.popleft()

        for k in range(8):#대각선 경우의 수 추가
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
    #대각선 경우의 수 추가
    dx = [0,0,-1,1,-1,-1,1,1]
    dy = [-1,1,0,0,1,-1,1,-1]
    
    #w,h 헷갈리지 않도록 주의!
    for i in range(h):
        for j in range(w):
            if island[i][j] == 1: #bfs가 실행되는 조건
                bfs(i,j,w,h) #w,h가 매번 달라지니까 넣어줌
                answer+=1 #섬을 찾을 때마다 +1

    print(answer)