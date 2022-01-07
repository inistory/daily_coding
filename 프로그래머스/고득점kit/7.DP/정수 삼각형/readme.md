## 1. 문제 설명

[문제 링크](https://www.acmicpc.net/problem/43105)

- 각형의 꼭대기에서 바닥까지 이어지는 경로 중, 거쳐간 숫자의 합이 가장 큰 경우를 찾아보려고 한다
- 아래 칸으로 이동할 때는 대각선 방향으로 한 칸 오른쪽 또는 왼쪽으로만 이동 가능
- triangle : 삼각형의 정보가 담긴 배열
- return : 거쳐간 숫자의 최댓값

## 2. 코드

```python
def solution(triangle):
    for i in range(1, len(triangle)): #첫째줄엔 1개, 둘째줄엔 2개 ...
        for j in range(i + 1): #j는 이전 값보다 하나 많은 갯수
            if j == 0:# 가장 왼쪽 값인 경우
                triangle[i][j] += triangle[i-1][j]
            elif j == i:# 가장 오른쪽 값인 경우
                triangle[i][j] += triangle[i-1][-1]
            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
    return max(triangle[-1]) #마지막 줄의 최댓값

```

## 3. 어려웠던 점

- j의 갯수를 어떻게 처리할지
