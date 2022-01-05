## 1. 문제 설명

[문제 링크](https://programmers.co.kr/learn/courses/30/lessons/60058)

- 입력 :

  - 균형잡힌 괄호 문자열: '(' 의 개수와 ')' 의 개수가 같은 문자열

- 출력 :
  - 올바른 괄호 문자열 : 균형잡힌 괄호 문자열이면서 '('와 ')'의 괄호의 짝도 모두 맞는 문자열

## 2. 코드

solution1.py

```python
def split_to_uv(p):
    stack = []
    left = 0
    right = 0
    correct = True #올바른 괄호 문자열인지 검사

    for i,pp in enumerate(p):
        if pp == '(':
            left+=1
            stack.append('(')
        else:
            right+=1
            if len(stack) == 0: #스택이 비어있으면, 올바르지 않은 괄호 문자열
                correct = False
            else: #올바른 괄호 문자열이면
                stack.pop()
        if left == right: #균형잡힌 문자열이 완성되는 순간
            return i+1, correct #v의 시작 인덱스, u의 올바른괄호문자열여부 전달


def solution(p):
    #1
    if len(p) == 0:
        return p
    #2
    v_idx, u_correct = split_to_uv(p)
    u = p[:v_idx]
    v = p[v_idx:]
    #3
    if u_correct == True:
        #3-1
        return u + solution(v)
    #4
    else:
        #4-1, 4-2, 4-3
        answer = '(' + solution(v) + ')'
        #4-4
        for i in range(1,len(u)-1):
            if u[i] == '(':
                answer+=')'
            else:
                answer+='('
        #4-5
        return answer

```

## 3. 회고

- 처음에 문제 속에 적힌 알고리즘을 제대로 보지않고, input, output만 보고 직접 알고리즘을 구현하려고 했었다.
- 문제를 잘 읽자..!
- 다른건 그대로 구현하면 되고, split_to_uv 는 u,v를 분리와 올바른 괄호 문자열인지 함께 체크해야한다.
- 올바른 괄호 문자열인지 판단하는 기준은 '(' 가 나오면 stack에 넣어주고, ')'가 나왔을 때, 스택이 비어있는지 아닌지 체크하는 것이다. 비어있다면 올바르지 않은 괄호 문자열!
- 처음에 split_to_uv()를 처음 호출하자마자 u와 v 둘다 균형잡힌 문자열이 되어야하는 줄 알았는데, 3번에 "문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. " 를 통해 처음 호출했을 때는 u만 균형잡힌 괄호 문자열이 된다는 것을 알 수 있었다.
- 이 문장을 통해 split_to_uv()에서는 u가 균형잡힌 문자열이라고 판단된 순간에 return 하면 된다는 것을 알 수 있다.
- u가 균형잡힌 문자열이 되기 위한 기준은 left, right 괄호가 서로 개수가 일치하는 첫 순간이다.

## 4. Reference

https://www.youtube.com/watch?v=Y-Xpiqsx8Hc
