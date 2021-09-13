import sys
v, e = map(int, sys.stdin.readline().split())
graph = { i:[] for i in range(v)}
for i in range(e):
    v1,v2 = map(int, sys.stdin.readline().split())
    graph[v1-1].append(v2-1)
    graph[v2-1].append(v1-1)

def count(graph,v,e):
   count = 0
   connection_check = 0#주어진 모든 노드가 연결되지 않았을경우
   for i in range(v):
       if len(graph[i])%2!=0:
           count+=1
       if len(graph[i])>0:
           connection_check+=1

   if connection_check>0 and count == 0 or count==2:
        return "YES"
   else:
        return "NO"

print(count(graph,v,e))   

