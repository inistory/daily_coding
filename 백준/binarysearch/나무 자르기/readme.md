## 1. 문제 설명

[문제 링크](https://www.acmicpc.net/problem/2805)

- 입력 :
  - 첫째 줄에 나무의 수 N과 상근이가 집으로 가져가려고 하는 나무의 길이 M
  - 둘째 줄에는 나무의 높이가 주어진다.
- 출력 :적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 출력

## 2. 코드

solution1.py

```python
# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline

n, m =map(int, input().split())
tree = list(map(int, input().split()))

start = 0
end = max(tree)
result = 0
while start <= end:
    mid = (start + end) //2
    #h기준으로 자른 후 가져갈 수 있는 나무 길이 total
    total = 0
    for i in range(n):
        if tree[i] > mid:
            total += tree[i] - mid

    if total == m:
        result = mid
        break
    elif total < m : #나무길이가 부족하면 mid를 앞쪽으로
        end = mid-1

    else: #나무양이 충분하면 저장
        start = mid+1
        result = mid

print(result)

```

solution2.py

```python
# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline

n, m =map(int, input().split())
tree = list(map(int, input().split()))

start = 0
end = max(tree)
result = 0
while start <= end:
    mid = (start + end) //2
    #h기준으로 자른 후 가져갈 수 있는 나무 길이 total
    total = 0
    for i in range(n):
        if tree[i] > mid:
            total += tree[i] - mid

    if total < m : #나무길이가 부족하면 mid를 앞쪽으로
        end = mid-1

    else: #나무양이 충분하면 저장
        start = mid+1
        result = mid

print(result)
```

## 3. 회고

- 나무의 높이가 1,000,000,000보다 작거나 같은 양의 정수 또는 0이기 때문에 이진탐색을 사용해서 탐색시간을 줄여야한다.
- 목재 절단기 높이를 mid로 보고 start와 end의 중간값으로 설정한다. (초기 start=0, end=max(tree))
- 절단기 높이 mid를 기준으로 잘랐을 때 얻을 수 있는 나무의 길이를 total에 저장한다.
- 가져가길 원했던 길이 m과 비교하여 길이가 같으면 result에 mid를 저장,
- 나무의 길이가 부족하면 더 작은 절단기 기준(mid)로 살펴봐야하므로, end = mid-1하여 현재보다 작은절단기 기준으로 나무를 자르도록 한다.
- 나무의 길이 충분하면 일단 start= mid+1를 통해 오른쪽도 탐색할 여지를 남겨두고, result에는 mid를 저장한다. (최대한 m과 비슷한 길이의 나무를 담는 것이 중요하므로, 후보가 생기면 일단 저장, 이진탐색을 하며 m과 더 가까운 수로 update)
- PyPy3로 제출해야 시간초과가 안난다.
  - solution1.py : 273888KB, 580ms
  - solution2.py : 273884KB, 356ms
