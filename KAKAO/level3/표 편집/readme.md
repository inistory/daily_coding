## 1. 문제 설명

[문제 링크](https://programmers.co.kr/learn/courses/30/lessons/81303)

- 입력
  - n : 처음 표의 행 개수를 나타내는 정수
  - k : 처음에 선택된 행의 위치를 나타내는 정수
- 출력
  - 수행한 명령어들이 담긴 문자열 배열 cmd가 매개변수로 주어질 때, 모든 명령어를 수행한 후 표의 상태와 처음 주어진 표의 상태를 비교하여 삭제되지 않은 행은 O, 삭제된 행은 X로 표시하여 문자열 형태로 return

## 2. 코드

solution1.py

```python
class Node:
    def __init__(self):
        self.removed = False
        self.prev = None
        self.next = None

def solution(n, k, cmd):
    nodeArr = [Node() for _ in range(n)]
    for i in range(1, n):
        nodeArr[i-1].next = nodeArr[i]
        nodeArr[i].prev = nodeArr[i-1]

    curr = nodeArr[k]
    mystack = []

    for str in cmd:
        if str[0] == 'U':
            x = int(str[2:])
            for _ in range(x):
                curr = curr.prev
        elif str[0] == 'D':
            x = int(str[2:])
            for _ in range(x):
                curr = curr.next
        elif str[0] == 'C':
            mystack.append(curr)
            curr.removed = True
            up = curr.prev
            down = curr.next
            if up:
                up.next = down #연결
            if down:
                down.prev = up#연결
                curr = down
            else:#마지막 값이면
                curr = up
        else: #Z
            node = mystack.pop()
            node.removed = False
            up = node.prev
            down = node.next
            if up:
                up.next = node
            if down:
                down.prev = node


    answer = ''
    for i in range(n):
        if nodeArr[i].removed: #True
            answer+='X'
        else:
            answer+='O'
    return answer
```

## 3. 회고

- 처음에는 자료구조를 사용하지 않고 풀려고 하다보니 계속 막혔다.
- 풀이를 보니, 연결리스트를 활용해 풀었다.
- class로 Node 객체를 선언해서 전후정보를 업데이트할 수 있고, 삭제한 후 현재 위치를 업데이트하기 편했다.
  - 삭제 후에는 현재 위치가 아래로 내려가는데, 마지막 노드가 삭제될 때는 현재위치를 위로 올려야한다.
- 연결리스트를 파이썬에서 구현하는 방법을 배웠고 재미있었다.
- 다음 번에도 활용할 수 있도록 구현연습을 해야겠다.

## 4. 참고

https://www.youtube.com/watch?v=A-KfaMVBfhg
