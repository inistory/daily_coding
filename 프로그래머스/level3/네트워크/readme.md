## 1. 문제 설명

[문제 링크](https://programmers.co.kr/learn/courses/30/lessons/43162)

- n: 컴퓨터의 갯수
- computers : 컴퓨터끼리 연결 정보 : [[1, 1, 0], [1, 1, 0], [0, 0, 1]] 에서는 1번 컴퓨터가 1,2번과 연결, 2번컴퓨터는 1,2번과 연결, 3번은 3번과 연결을 의미
- return : 연결된 컴퓨터 집합의 개수 : 위 예시의 경우는 2 (1번,2번),(3번) => 2개

## 2. 코드

```python
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
```

## 3. 어려웠던 점

- union, find 에 익숙하지 않아 처음에 활용해서 풀지 못함

- 마지막에 return len(set(root)) 했을 때는 에러 케이스가 존재
