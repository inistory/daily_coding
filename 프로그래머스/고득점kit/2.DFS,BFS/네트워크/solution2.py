def find(root, x):
	if root[x] == x:
		return root[x] 
	root[x] = find(root, root[x]) 
	return root[x]

def union(root,x,y):
	rx, ry = find(root,x), find(root,y)  
	if rx != ry:
		root[ry] = rx

        
def solution(n, computers):
    root = [i for i in range(n)]
    for i in range(n):
        for j in range(n):
            if computers[i][j] and i!=j:
                if find(root, i) != find(root,j):
                    union(root, i,j)
    answer = len([i for i in range(n) if i==root[i]])
    return answer       
    #return len(set(root)) #왜 안되지