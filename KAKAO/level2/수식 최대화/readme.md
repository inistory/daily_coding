## 1. 문제 설명

[문제 링크](https://programmers.co.kr/learn/courses/30/lessons/67257)

- input : 수식
- return : 연산자의 우선순위를 중복되지 않도록 임의로 선정하여 계산하는 경우의 수 중에서 최댓값 출력

## 2. 코드

```python
import re
from itertools import permutations

def solution(expression):
    operator = [x for x in ['*','+','-'] if x in expression]
    operators = [list(y) for y in permutations(operator)]
    expression = re.split(r'(\D)',expression) #(\D): 숫자가 아닌것 기준으로 split

    answer = []
    for operator in operators:
        ex_copy = expression #복사
        for op in operator:
            while op in ex_copy: #부호가 존재하는 동안 반복
                i = ex_copy.index(op) #연산자가 존재하는 곳의 인덱스
                #연산자 바로 전 자리에 계산한 결과를 저장
                ex_copy[i-1] = str(eval(ex_copy[i-1] + ex_copy[i] + ex_copy[i+1]))
                ex_copy = ex_copy[:i] + ex_copy[i+2:] #이미 계산한 부분 제거

        answer.append(ex_copy[0])

    return max(abs(int(x)) for x in answer)

```

## 3. 회고

- str to list를 진행할 때, 특정 규칙을 그룹화하기

  - expression = re.split(r'(\D)',expression)
  - '[]' : 괄호 안의 문자들을 하나하나씩 인식함. '[abcd]' 라는게 있으면, a 혹은 b 혹은 c 혹은 d 로 인식됨.
  - '()' : 특수문자 안에 있는 글자를 하나의 덩어리로 인식함. a 혹은 b 혹은 c 혹은 d 로 인식되게 하려면, (a|b|c|d) 이런식으로 작성을 해야함
  - 처음에는 [숫자그룹][부호그룹] 이렇게 나누려다가 자꾸 한 자리 숫자를 숫자 하나로 보는 에러가 났었다. 내가 원하는 건 여러숫자들을 숫자 하나로 보는 것이었는데, 그렇게 하고 싶을 때는, 숫자가 아닌 것을 기준'(\D)'으로 split해야한다.

- ex_copy에서 이미 계산한 부분 제거하기

  - ex_copy = ex_copy[:i] + ex_copy[i+2:]
  - i-1,i,i+1 의 연산결과를 ex_copy[i-1]에 계산 결과를 넣어주었으니, i와,i+1번째 요소들은 지워야 한다.
  - 계산한 부분을 제거할 때는 del를 써서 특정인덱스를 지워주는 것보다 필요한 부분만 잘라서 붙여주는 것이 좋다.

- 얕은 복사와 깊은 복사
  - 얕은 복사:a 라는 객체를 생성한 후 b = a 와 같이 할당하면 이는 a 객체가 통째로 b 로 복사되는 것이 아니다. 단지 b 또한 a 객체를 참조만 할 뿐. 따라서, 아래와 같이 a 리스트의 첫번째 값을 바꾸면 b 의 첫번째 값도 같은 것을 가리키는 것이므로 바뀌어 있다.
  - 깊은 복사: 객체를 완전하게 복사
    - 리스트일 경우, b = a[:] 사용
    - 리스트가 아닌 경우는 copy 모듈 사용 (b = copy.deepcopy(a))

## 4. 참고

https://velog.io/@cyanred9/SQL-%EC%A0%95%EA%B7%9C%ED%91%9C%ED%98%84%EC%8B%9D%EC%9D%98-%EC%86%8C%EA%B4%84%ED%98%B8-%EB%8C%80%EA%B4%84%ED%98%B8-%EC%B0%A8%EC%9D%B4

http://cloudrain21.com/python-functions-to-memorize-1
