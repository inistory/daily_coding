탐욕법(Greedy)

[https://programmers.co.kr/learn/courses/30/lessons/42861](https://programmers.co.kr/learn/courses/30/lessons/42861)

## 1. 문제 설명

- 입력
  costs: n개의 섬 사이에 다리를 건설하는 비용
- 출력
  최소 비용으로 모든 섬이 서로 통행 가능하도록 만들 때 필요한 최소 비용을 return
- 규칙
  1. 다리를 여러 번 건너더라도, 도달할 수만 있으면 통행 가능하다고 봅니다. 예를 들어 A 섬과 B 섬 사이에 다리가 있고, B 섬과 C 섬 사이에 다리가 있으면 A 섬과 C 섬은 서로 통행 가능
  2. 섬의 개수 n은 1 이상 100 이하
  3. 임의의 i에 대해, costs[i][0] 와 costs[i] [1]에는 다리가 연결되는 두 섬의 번호가 들어있고, costs[i] [2]에는 이 두 섬을 연결하는 다리를 건설할 때 드는 비용
  4. 같은 연결은 두 번 주어지지 않습니다. 또한 순서가 바뀌더라도 같은 연결로 봅니다. 즉 0과 1 사이를 연결하는 비용이 주어졌을 때, 1과 0의 비용이 주어지지 않습니다.
  5. 모든 섬 사이의 다리 건설 비용이 주어지지 않습니다. 이 경우, 두 섬 사이의 건설이 불가능한 것으로 봅니다.

## 2. 코드

```python
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

```

## 3. 어렵거나 헷갈렸던 점

1. 그리디 알고리즘으로 이 문제를 풀어가는 방법
2. 노드를 돌아가면서 작은 cost를 선택해야겠다고 생각은 했는데, 모든 섬이 통행가능한 한 것을 어떻게 검사를 할 지 어려웠다.
   → MST(최소 신장 트리) 중 하나인 크루스칼 알고리즘을 이용해 푸는 문제
3. union, find 개념을 활용하니 훨씬 간단하다.
