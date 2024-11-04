def dfs(start):
    stack = [start]
    visited = [0]*(V+1)
    visited[start] = 1
    count = 0
    while stack:
        node = stack.pop()
        for i in range(1,V+1):
            if graph[node][i]==1 and not visited[i]:
                visited[i] = 1
                stack.append(i)
                count+=1
    return count


V  = int(input())
E = int(input())
graph = [[0]*(V+1) for _ in range(V+1)]

for i in range(E):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

print(dfs(1))
    