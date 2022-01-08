#미로탈출문제
#n*m의 미로
#동빈 위치: (1,1)
#미로 출구 : (N,M)
#괴물이 있는 부분:0, 없는 부분:1
#탈출하기 위해 이동해야하는 최소 칸수(시작칸 마지막칸 포함)
from collections import deque

n,m = map(int,input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input()))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dx[i]
            if nx <0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx] = graph[x][y] + 1
                queue.append((nx,ny))

    return graph[n-1][m-1]

print(bfs(0,0))
#모든 간선의 비용이 동일할 때만 최단거리를 푸는 문제는 bfs로 풀어야함, 간선의 비용이 다르면 다익스트라
#모든 경로 탐색 시에는 dfs, bfs 모두 사용가능