## 1. 문제 설명

[문제 링크](https://www.acmicpc.net/problem/14502)

- 입력
  - 첫째 줄에 지도의 세로 크기 N과 가로 크기 M이 주어진다. (3 ≤ N, M ≤ 8)
  - 둘째 줄부터 N개의 줄에 지도의 모양이 주어진다. 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 위치이다. 2의 개수는 2보다 크거나 같고, 10보다 작거나 같은 자연수이다.빈 칸의 개수는 3개 이상이다.
- 출력 : 첫째 줄에 얻을 수 있는 안전 영역의 최대 크기를 출력한다.

## 2. 코드

solution1.py

```python
# -*- coding: utf-8 -*-

n, m = map(int, input().split())
data = [] # 초기 맵 리스트
temp = [[0] * m for _ in range(n)] # 벽을 설치한 뒤의 맵 리스트

for _ in range(n):
    data.append(list(map(int, input().split())))

# 4가지 이동 방향에 대한 리스트
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

# 깊이 우선 탐색(DFS)을 이용해 각 바이러스가 사방으로 퍼지도록 하기
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 상, 하, 좌, 우 중에서 바이러스가 퍼질 수 있는 경우
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                # 해당 위치에 바이러스 배치하고, 다시 재귀적으로 수행
                temp[nx][ny] = 2
                virus(nx, ny)

# 현재 맵에서 안전 영역의 크기 계산하는 메서드
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

# 깊이 우선 탐색(DFS)을 이용해 울타리를 설치하면서, 매 번 안전 영역의 크기 계산
def dfs(count):
    global result
    # 2. 울타리가 3개 설치된 경우 바이러스 전파
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        # 각 바이러스의 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        # 3. 안전 영역의 최대값 계산
        result = max(result, get_score())
        return
    # 1. 빈 공간에 울타리를 설치
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1

dfs(0)
print(result)
```

## 3. 회고

- 아직 이 문제를 혼자서 풀기에는 어려워서 이코테 책 풀이를 보고 최대한 이해한 후 외워버렸다.
- 전체적인 코드의 풀이 방향은 세 가지로 요약할 수 있다.

1. 빈공간에 울타리 설치

- for 문으로 data(초기 맵 리스트)를 돌면서 0이 나오는 순간 1로 대체한다.
- 0인 모든 부분 중 세 곳를 선택해서 1을 넣을 때, 나올 수 있는 모든 조합을 탐색해야한다.(완전탐색!)
- 그래서 count 변수를 dfs를 재귀호출 할 때, 넣어주어 count==3이 될 때 과정2를 수행하도록 한다.
- dfs()를 마친 후에 원상복귀하는 이유는 data와 count의 초기 상태를 계속 활용해야하기 때문이다.

2. 울타리가 3개 설치된 경우 바이러스 전파: 상하좌우

- 울타리 세 개가 설치된 시점에 조건문을 넣어서 temp에 울타리를 넣은 상태(세 개의 1을 넣은 상태)의 data를 복붙(?)해준다.
- 초기상태를 계속 써서 다른 조합을 매번 찾아야하기 때문에 따로 해준 것 같다.
- temp로 정보를 모두 옮긴 뒤에는 바이러스의 위치(2가 있는 위치)에서 근처에 0이 있을 때, 전파를 진행해야한다. 이건 virus함수에서 수행된다.
- virus() 함수에는 temp에서 2가 발견된 순간의 x,y 좌표를 전달해준다.
- 해당 좌표를 상하좌우를 탐색하여 0을 발견하면 2로 변경하는 작업을 재귀적으로 수행한다.

3. 안전 영역의 최대값 계산: 0의 개수

- 전파가 가능한 곳을 모두 2로 만든 후에는 남아있는 0의 개수를 세서 안전영역을 계산해야한다.
- getscore()는 현재 temp의 상태를 기준으로 0의 개수를 세서 반환한다.
- 반환된 결과는 다른 조합에서의 score가 저장되어 있을 result와 비교하여 최대값을 result에 저장할 수 있도록 한다.
- 그래야 모든 경우를 탐색하여 안전 영역의 최대 크기를 찾을 수 있다.
- return을 해준 이유는 울타리를 세 개 설치했을 때까지만 if문을 실행하고, 그 이상의 경우는 탐색하지 않기 위해서이다.

## 4. 참고

https://github.com/ndb796/python-for-coding-test/blob/master/13/2.py
