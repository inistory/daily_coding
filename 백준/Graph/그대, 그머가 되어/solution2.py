#BFS
import sys
from collections import deque
INF = int(1e9)
a,b = map(int,sys.stdin.readline().split())
n,m = map(int,sys.stdin.readline().split())

board = [[] for _ in range(n+1)]
for _ in range(m):
    x,y = map(int,sys.stdin.readline().split())
    board[x].append(y)
    board[y].append(x)

count = INF
visited = [False]*(n+1) #최단 거리 테이블
visited[a] = True
q = deque([(0,a)])

while q: #큐가 비어있지 않다면
    dist, cur_node = q.popleft()
    if cur_node == b:
        count = min(count,dist)
    for next in board[cur_node]:
        if not visited[next]: #방문하지 않았다면
            visited[next] = True #방문상태로 바꿔줌
            q.append((dist+1,next))

if count == INF:
    print(-1)
else:
    print(count)