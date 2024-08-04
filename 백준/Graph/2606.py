def dfs(start):
    stack = []
    visited = [0]*(V+1)
    stack.append(start)
    while stack:
        now = stack.pop()
        visited[now] = 1
        for i in range(1,V+1):
            if not visited[i] and node[now][i]:
                stack.append(i)
        
    return sum(visited)-1

V = int(input()) #컴퓨터의수
E = int(input()) #연결되어 있는 컴퓨터 쌍의 수
node = [[0]*(V+1) for _ in range(V+1)]
for _ in range(E):
    start, end = map(int, input().split())
    node[start][end] = 1
    node[end][start] = 1
print(dfs(1))