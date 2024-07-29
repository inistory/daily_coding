def DFS(start, end): 
    stack = []       
    visited = [0]*(V+1)  
    stack.append(start)    

    while stack:          
        now=stack.pop()   
        visited[now] = 1 
        for i in range(1, V+1):  
            if not visited[i] and node[now][i]: 
                stack.append(i) 
    if visited[end]: 
        return 1    
    else:
        return 0    

test_case=int(input())
for t in range(1,test_case+1):
    V, E = map(int,input().split())
    node=[[0] * (V+1) for _ in range(V+1)] 
    for _ in range(E): 
        start, end = map(int, input().split())
        node[start][end]=1
    print('node:', node)

    start, end = map(int, input().split())
    print("#{} {}".format(t, DFS(start,end)))