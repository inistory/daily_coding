#트리의 부모찾기

#######BFS
import sys
input = sys.stdin.readline
n = int(input())
graph = [[0] for _ in range(n + 1)]
visited = [0] * (n+1)
stack = []

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited[1] = 1
stack.append(1)
while stack:
    node = stack.pop()
    for i in graph[node]:
        if not visited[i]:
            visited[i] = node
            stack.append(i)

for i in range(2, n+1):
    print(visited[i])
    
#########DFS

import sys
sys.setrecursionlimit(10 ** 9)
 
n=int(sys.stdin.readline())#노드의 갯수
tree=[[] for _ in range(n+1)]
for _ in range(n-1):
    n1,n2 =map(int,sys.stdin.readline().split())
    tree[n1].append(n2)
    tree[n2].append(n1)
 
 
#부모저장
parents=[0 for _ in range(n+1)]
 
def DFS(start,tree,parents):
    for i in tree[start]:#연결된 노드 모두탐색
        if parents[i]==0:#한번도 방문한적이 없다면
           parents[i]=start#부모노드 저장
           DFS(i,tree,parents)
 
 
DFS(1,tree,parents)
 
for i in range(2,n+1):
    print(parents[i])