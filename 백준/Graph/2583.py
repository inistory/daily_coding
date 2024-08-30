# 영역 구하기
from collections import deque

M, N, K = map(int,input().split())
graph = [[0]*N for _ in range(M)]

for _ in range(K):
    x,y,x2,y2 = map(int,input().split())

    for yy in range(y,y2):
        for xx in range(x,x2):
            graph[yy][xx] =1

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def bfs(xxx,yyy):
    queue = deque()
    queue.append((xxx,yyy))
    graph[xxx][yyy] = 1
    count = 1
    
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx <M and 0<=ny<N and not graph[nx][ny]:
                queue.append((nx,ny))
                graph[nx][ny] = 1
                count += 1
    return count

answer = []
for xxx in range(M):
    for yyy in range(N):
        if graph[xxx][yyy] == 0:
            answer.append(bfs(xxx,yyy))

answer.sort()
print(len(answer))
for ans in answer:
    print(ans, end=' ')

    
