## 1. 문제 설명

[문제 링크](https://www.acmicpc.net/problem/2003)

- 입력
  - n: n개로 된 수열
  - m: 합
- 출력
  - N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다. 이 수열의 i번째 수부터 j번째 수까지의 합 A[i] + A[i+1] + … + A[j-1] + A[j]가 M이 되는 경우의 수

## 2. 코드

solution1.py

```python
#-*- coding: utf-8 -*-
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

ary = list(map(int,input().split()))

hab = 0
end = 0
result = 0
# start를 차례대로 증가시키며 반복
for start in range(n):
    #end를 가능한 만큼 오른쪽으로 이동시키기
    while hab < m and end < n:
        hab += ary[end]
        end+=1
    if hab == m:
        result+=1
    #부분합이 m과 같거나 클 때, start를 오른쪽으로 이동
    hab -= ary[start]

print(result)
```

## 3. 회고

- 구간의 합 < m : end 오른쪽으로 이동 (합을 늘림)
- 구간의 합 > m : start 오른쪽으로 이동 (합을 줄임)
- 구간의 합 = m : 카운트 증가

## 4. 참고

https://www.youtube.com/watch?v=rI8NRQsAS_s
