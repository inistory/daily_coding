## 1. 문제 설명

[문제 링크](https://programmers.co.kr/learn/courses/30/lessons/81302)

- 입력: 5개의 대기실 정보
- 출력: 각 대기실에서 거리두기를 잘 했으면 1, 아니면 0을 출력

## 2. 코드

```python
import queue

D = ((-1,0),(1,0),(0,-1),(0,1))#상하좌우로 이동하기 위한 delta array

def bfs(place, row, col): #P의 위치에서 bfs실행
    visited = [[False for _ in range(5)] for _ in range(5)] #5x5
    q = queue.Queue()
    visited[row][col] = True #큐 꺼내기전에 마킹
    q.put((row,col,0)) #행, 열, 거리

    while not q.empty():
        curr = q.get()

        if curr[2] > 2: #거리가 2를 초과하면 스킵
            continue
        if curr[2] !=0 and place[curr[0]][curr[1]] == 'P': #시작위치가 아닌 다른 P를 만났을 때
            return False

        #길이 2이하일 때
        for i in range(4):
            nr = curr[0] +D[i][0]
            nc = curr[1] +D[i][1]
            if nr < 0 or nr >4 or nc <0 or nc >4:#범위를 벗어난다면
                continue
            if visited[nr][nc]: #이미 큐에 넣은 적이 있다면 다시 넣을 필요가없음
                continue
            if place[nr][nc] == 'X':#파티션이 있으면 이동할 수 없음
                continue
            visited[nr][nc] = True
            q.put((nr,nc, curr[2]+1))
    return True


def check(place):
    for r in range(5):
        for c in range(5):
            if place[r][c] == 'P':
                if bfs(place,r,c) == False: #거리두기 안지켜짐
                    return False
    return True #조건문에 걸리지 않아서 모두 탐색을 완료하게 된다면 True 리턴


def solution(places):
    answer = []

    for place in places:
        if check(place): #거리두기를 지키고 있는지
            answer.append(1)
        else:
            answer.append(0)

    return answer
```

## 3. 회고

- P를 발견하면 거리가 2이하인 부분만 bfs로 거리두기가 잘 진행되고 있는지 코드를 짜야겠다고 생각
- bfs 구현 부분에서 막혔다.

- 길이를 어떻게 추적할지? (2이하만 탐색하게 하려면)

  - 큐에 거리정보를 추가
  - 큐에는 새롭게 탐색할 좌표와 P로부터 해당 좌표까지의 거리가 저장되어 있다.
  - 큐에서 정보를 꺼냈을 때, 거리가 2를 초과하는지 확인 후,
    - 초과한다면 continue를 통해 해당 좌표를 기준으로 상하좌우를 탐색하지 못하도록 한다.
    - 거리가 2이내인 좌표의 상하좌우만을 탐색하도록 한다.

- 주변을 어떤 방식으로 탐색할지?

  - delta array를 활용해서 상하좌우를 탐색
  - 새롭게 발견한 탐색가능한 부분의 좌표(nr,nc),현재까지의 거리+1(curr[2]+1)해서 큐에 담기
    - nr,nc가 범위를 벗어났을 경우, 이미 방문한 좌표인경우, 해당 위치에 파티션이 존재하는 경우는 continue를 통해 아래 내용 건너뛰기(큐에 넣지 못하도록)

- 파티션이 있을 때 예외처리는 어떻게 할지?

  - P와 또 다른 P가 거리 2 이내에 있을 때, X를 검색하는 방식으로 하려니 어떻게 할지 생각이 안남
  - 풀이를 보니, 대기실 별로 P를 먼저 찾고(check함수), 그 때의 좌표 정보를 가지고, 길이 2이내일 때 상하좌우를 탐색하는 반복문(bfs함수 내의 for문)에서 파티션이 있으면 큐에 넣지 않도록 조건문을 추가해야함
    - if place[nr][nc] == 'X' : continue
    - 해당 방향의 탐색을 중지시킴

## 4. 참고

https://www.youtube.com/watch?v=hCVgKE6qwFs
