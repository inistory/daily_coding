## 1. 문제 설명

[문제 링크](https://www.acmicpc.net/problem/1068)

- 첫째 줄 : 트리의 노드의 개수
- 둘째 줄 : 각 노드의 부모
- 셋째 줄 : 지울 노드의 번호
- return : 첫째 줄에 입력으로 주어진 트리에서 셋째 줄에 입력으로 주어진 노드를 지웠을 때, 리프 노드의 개수

## 2. 코드

```python
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

```

## 3. 어려웠던 점

- 리프 노드를 어떻게 찾을 것인지 -> dfs 사용

- 노드를 어떻게 지울 것인지 -> 지우는것 대신 해당 노드와 자식노드들을 -2로 변경
  s
