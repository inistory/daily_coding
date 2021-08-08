## 1. 문제 설명

[문제 링크](acmicpc.net/problem/2251)

- 첫째 줄: 물 통 세개의 각각의 부피
- return : 처음에는 앞의 두 물통은 비어 있고, 세 번째 물통은 가득(C 리터) 차 있다. 한 물통이 비거나, 다른 한 물통이 가득 찰 때까지 물을 부을 수 있다. 첫 번째 물통(용량이 A인)이 비어 있을 때, 세 번째 물통(용량이 C인)에 담겨있을 수 있는 물의 양을 모두 출력

## 2. 코드

```python
import sys
from collections import deque

# x, y의 경우의 수 저장
def pour(x, y):
    if not visited[x][y]:
        visited[x][y] = True
        q.append((x, y))

def bfs():

    while q:
        # x : a물통의 물의 양, y : b물통의 물의 양, z : c물통의 물의 양
        x, y = q.popleft()
        z = c - x - y

        # a 물통이 비어있는 경우 c 물통에 남아있는 양 저장
        if x == 0:
            answer.append(z)

        # x -> y
        water = min(x, b-y)
        pour(x - water, y + water)
        # x -> z
        water = min(x, c-z)
        pour(x - water, y)
        # y -> x
        water = min(y, a-x)
        pour(x + water, y - water)
        # y -> z
        water = min(y, c-z)
        pour(x, y - water)
        # z -> x
        water = min(z, a-x)
        pour(x + water, y)
        # z -> y
        water = min(z, b-y)
        pour(x, y + water)


# 입력(리터 범위)
a, b, c = map(int, sys.stdin.readline().split())

# 경우의 수를 담을 큐
q = deque()
q.append((0, 0))

# 방문 여부(visited[x][y])
visited = [[False] * (b+1) for _ in range(a+1)]
visited[0][0] = True

# 답을 저장할 배열
answer = []

bfs()

# 출력
answer.sort()
print(*answer)


```

## 3. 어려웠던 점

- 문제이해 : 한 물통이 비거나, 다른 한 물통이 가득 찰 때까지 물을 부을 수 있다 ??

  - 서로 용량이 다른 물통이니까 특정 물통에 다 붓고도 남을 수 있다. : 용량이 작은 물통에 꽉찬 큰 물통을 부으면 남을 수 있음, 반대로 용량이 작은 물통을 큰 용량 물통에 부으면 큰 물통에 적은 양이 담길 수 있는 것
