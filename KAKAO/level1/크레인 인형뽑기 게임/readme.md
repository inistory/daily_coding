## 1. 문제 설명

[문제 링크](https://programmers.co.kr/learn/courses/30/lessons/64061#)

- 입력: boards [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]] 보드에 있는 인형 정보
- 출력: moves [1,5,3,5,1,2,1,4] 인형을 어디 위치에서 뽑을지

## 2. 코드

```python
def solution(boards, moves):
    moves = list(map(lambda x : x-1, moves)) #1씩 빼주기
    stack = [0] #index out of range 방지하여 0 넣어주기(맨 처음에도 stack[-2]를 검사할경우에 발생)
    cnt = 0
    for i in moves:
        for board in boards:
            if board[i] !=0:
                stack.append(board[i])
                board[i] = 0
                if stack[-1] == stack[-2]:  #스택의 가장위, 그 아래 수를 비교
                    stack.pop()
                    stack.pop()
                    cnt+=2
                break
    return cnt
```

## 3. 회고

- 처음에 인덱스를 맞춰주기 위해서 moves 값을 모두 -1 씩 해주었다. map, lambda를 검색하지 않고도 쓸수있도록 연습해야겠다.
- break 문을 자주 사용해보진않았는데, 이 문제의 경우 꼭 필요했다.
- 한 번 발견하고 board에서 값을 빼고 stack에 넣었다면, break로 for문을 빠져나와 다음 move를 확인해야한다. 그렇지 않으면 현재 move 에 해당하는 board를 더 탐색해서 지울 것이기 때문에 break를 꼭 해주어야한다.
