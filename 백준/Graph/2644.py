#촌수계산
n = int(input())
a, b = map(int,input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
for i in range(m):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(curr,count):
    visited[curr] = 1
    if curr == b:
        return count
    
    for i in graph[curr]:
        if not visited[i]:
            result = dfs(i,count+1)
            if result != -1:  # 촌수를 찾은 경우
                return result   
    return -1 

print(dfs(a,0))