import sys
from collections import deque
from itertools import combinations
from copy import deepcopy
input = sys.stdin.readline

N,M = map(int,input().split())

origin_map = [list(map(int,input().split())) for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
answer = 0
#빈칸중에 벽세우는 조합만들기
blank = [(i,j) for i in range(N) for j in range(M) if origin_map[i][j] == 0]
for walls in combinations(blank,3):
    tmp_map =deepcopy(origin_map)
    q = deque() #이전 큐를 남기지 않기 위해 여기에 선언
    for r,c in walls:
        tmp_map[r][c] = 1

    #2인칸에서만 바이러스가 전파가 시작하니까 그것만 큐에 넣어주기
    for i in range(N):
        for j in range(M):
            if tmp_map[i][j] == 2:
                q.append((i, j))
        
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y+dy[k]
            
            if 0<=nx<N and 0<=ny<M:
                if tmp_map[nx][ny] == 0:
                    tmp_map[nx][ny] = 2
                    q.append((nx,ny))
                    
    zero_count = sum(row.count(0) for row in tmp_map)
    answer = max(answer,zero_count)
print(answer)