N = int(input())
arr = list(map(int,input().split()))
k = int(input())


#지울노드를 찾아 해당 노드의 자식들도 지움 처리 -> -2
def dfs(k,arr):
    arr[k] = -2
    for i in range(len(arr)):
        if arr[i] == k:
            dfs(i,arr)

dfs(k,arr)

#리프 노드 찾기 : -2가 아니고, arr에 포함되어 있지 않은 수를 count
count = 0 
for i in range(N):
    if arr[i] !=-2 and i not in arr:
        count+=1
print(count)
