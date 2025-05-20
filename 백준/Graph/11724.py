#연결 요소의 개수
from collections import deque

N, M = map(int, input().split())

graph = [[0] for _ in range(N+1)]
visited = [0]*(N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0
for i in range(1, N+1):
    if not visited[i]:
        queue = deque()
        queue.append(i)
        
        while queue:
            c = queue.popleft()
            for j in graph[c]:
                if not visited[j]:
                    visited[j] = 1
                    queue.append(j)
        count+=1
    
print(count)


