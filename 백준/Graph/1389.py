#케빈 베이컨의 6단계 법칙
N, M = map(int, input().split())
graph = [[]for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

from collections import deque
queue = deque()

def bfs(n,count):
    visited = [0]*(N+1)
    queue.append((n,count))
    visited[n] = 1
    total_count = 0 
    
    while queue:
        n, count = queue.popleft()
        total_count += count
        
        for i in graph[n]:
            if not visited[i]:
                visited[i] = 1
                queue.append((i,count+1))
    return total_count

min_bacon = float('inf')
bacon_idx = 0
for idx in range(1,N+1):
    bacon = bfs(idx,0)
    if bacon < min_bacon:
        min_bacon = bacon
        bacon_idx = idx

print(bacon_idx)
    

    
    
    
    