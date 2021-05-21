def find(root, x):
	if root[x] == x:
		return x 
	root[x] = find(root, root[x]) 
	return root[x]

def union(root,x,y):
	rx, ry = find(root,x), find(root,y)  
	if rx != ry:
		root[ry] = rx

def solution(n, costs):
    answer = 0
    cnt = 0 
    root = [i for i in range(n)]
    costs = sorted(costs, key=lambda x:x[2])
    
    for cost in costs:
        if find(root, cost[0]) != find(root,cost[1]):
            union(root, cost[0],cost[1])
            answer+=cost[2]
            cnt += 1
        if cnt == n-1: 
            return answer

    return answer
