## 1. 문제 설명

[문제 링크](https://programmers.co.kr/learn/courses/30/lessons/92344)

- 입력
  - 건물의 내구도를 나타내는 2차원 정수 배열 board와
  - 적의 공격 혹은 아군의 회복 스킬을 나타내는 2차원 정수 배열 skill
- 출력
  - 적의 공격 혹은 아군의 회복 스킬이 모두 끝난 뒤 파괴되지 않은 건물의 개수를 return

## 2. 코드

solution1.py

```python
def solution(board, skill):
    answer = 0
    tmp = [[0]*(len(board[0])+1) for _ in range(len(board)+1)]

    for type, r1,c1,r2,c2,degree in skill:
        tmp[r1][c1] += degree if type ==2 else -degree
        tmp[r1][c2+1] += -degree if type==2 else degree
        tmp[r2+1][c1] += -degree if type==2 else degree
        tmp[r2+1][c2+1] += degree if type==2 else -degree

    #행 기준 누적합
    for i in range(len(tmp)-1):
        for j in range(len(tmp[0])-1):
            tmp[i][j+1] += tmp[i][j]

    #열 기준 누적합
    for j in range(len(tmp[0])-1):
        for i in range(len(tmp)-1):
            tmp[i+1][j]+=tmp[i][j]

    #기존 배열과 합함
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += tmp[i][j]
            # board에 값이 1이상인 경우 answer++
            if board[i][j] > 0: answer += 1
    return answer
```

## 3. 회고

- 처음 풀 때 정확성은 통과하는데 효율성은 모두 통과를 못했다.
- 풀이를 보니, 누적합이라는 것을 쓴다.

  - 누적합이란?

    - 만약 [1, 3, 5, 5]의 1차원 배열에서 0번~2번 인덱스까지 2만큼 피해를 주고 싶다면
    - 보통은 O(N)의 시간복잡도를 사용하여 전부를 탐색한다.
    - 누적합을 사용하면 O(1)로 해결 가능

  - 1차원 배열의 경우(예시)
    - [0,0,0,0] 1차원 배열과 길이가 같은 0으로 전부 초기화된 배열을 생성한다.
    - 시작 부분에 빼려는 값을 넣고, 종료 지점보다 한 칸 뒤에 반대 부호를 가진 값을 넣는다.
    - [-2,0,0,2]
    - 누적합 진행 : [-2, -2, 0, 2] -> [-2, -2, -2, 2] -> [-2, -2, -2, 0]
    - 기존 배열에 합함: [1, 3, 5, 5] + [-2, -2, -2, 0] = [-1, 1, 3, 5]
  - 2차원 배열의 경우

    - (0,0) ~ (2,2)까지 n만큼 변화를 주고 싶다면,아래와 같이 n배치
      [n, 0, 0, -n]
      [0, 0, 0, 0]
      [0, 0, 0, 0]
      [-n, 0, 0, n]

    - 열기준, 행기준 누적합을 진행
      [n, n, n, 0]
      [n, n, n, 0]
      [n, n, n, 0]
      [0, 0, 0, 0]

  - 결론
    - 즉 (x1, y1) ~ (x2, y2)까지에 n만큼의 변화를 주고 싶다면,(x1, y1) = n, (x2+1, y1) = -n, (x1, y2+1) = -n, (x2+1, y2+1) = n 만큼의 값을 더해준다.
    - 그 후 행, 열 누적합 진행 후, 배열을 기존 board배열에 더해준다.

## 4. 참고

https://programmers.co.kr/questions/25471
https://kimjingo.tistory.com/155
