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

- 주변을 어떤 방식으로 탐색할지?

  - delta array로 상하좌우를 탐색

- 파티션이 있을 때 예외처리는 어떻게 할지?

  - P와 또 다른 P가 거리 2 이내에 있을 때, X를 검색하는 방식으로 하려니 어떻게 할지 생각이 안남
  - 풀이를 보니, P를 먼저 찾고, 길이 2이내에 P가 있는지 검사를 하는 반복문 내에서 파티션이 있으면 이동을 중단하도록 조건문을 추가해야함: 이동을 안하면 다른 방향을 탐색하니까 기존방향에서 P가 나오더라도 탐지하지 못함

- 길이를 어떻게 추적할지?
  - 큐에, 거리가 2이하일 때의 (x좌표,y좌표, 거리정보)를 넣어줌
  - 모든 조건(탐색이 지속되지 않을 경우의 조건들)을 모두 통과하면 방문처리와 함께 큐에 넣어줌,그 때 거리를 늘려줌

## 4. 참고

https://www.youtube.com/watch?v=hCVgKE6qwFs
