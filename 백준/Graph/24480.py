#알고리즘 수업 - 깊이 우선 탐색 2
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)#런타임에러방지

V, E, R = map(int, input().split())
graph = [[] for _ in range(V+1)]
visited = [0]*(V+1)
count = 1

for _ in range(E):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(R):
    global count #함수 안에서 전역변수 쓰고 싶을 때
    visited[R] = count
    graph[R].sort(reverse=True) 
    for x in graph[R]:
        if not visited[x]:
            count+=1
            dfs(x)

dfs(R)         
for i in range(1,V+1):
    print(visited[i])

