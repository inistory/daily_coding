from collections import deque

n, m = map(int, input().split())

arr = [list(map(int, input().strip())) for _ in range(n)]
visited = [[0] * m  for _ in range(n)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


q = deque([(0, 0, 1)])
visited[0][0] = 1

while q:
    r, c, count = q.popleft()
    
    if r==n-1 and c==m-1:
        print(count)
        break
    
    for i in range(4):
        nr, nc = r+dr[i], c+dc[i]
        
        if 0 <= nr < n and 0 <= nc < m and arr[nr][nc]==1 and not visited[nr][nc]:
            visited[nr][nc] = 1
            q.append((nr,nc,count+1))