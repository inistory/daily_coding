## 1. 문제 설명

[문제 링크](https://programmers.co.kr/learn/courses/30/lessons/17684)

- 입력
  - 첫째 줄에 수의 개수 N(2 ≤ N ≤ 11)가 주어진다.
  - 둘째 줄에는 A1, A2, ..., AN이 주어진다. (1 ≤ Ai ≤ 100)
  - 셋째 줄에는 합이 N-1인 4개의 정수가 주어지는데, 차례대로 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수
- 출력 :
  - 첫째 줄에 만들 수 있는 식의 결과의 최댓값을, 둘째 줄에는 최솟값을 출력

## 2. 코드

solution1.py

```python
def solution(msg):
    answer = []
    dictionary = {chr(e + 64): e for e in range(1, 27)} #1.사전 초기화
    num = 27
    while msg: #msg 문자열이 빌 때까지 반복
        tt = 1
        #사전에 msg[:tt]가 존재하면 tt를 증가시킴
        while msg[:tt] in dictionary.keys() and tt <= len(msg):
            tt += 1
        tt -= 1
        #msg[:tt]는 사전에 있지만 msg[:tt+1]은 사전에 없는 경우
        if msg[:tt] in dictionary.keys():
            answer.append(dictionary[msg[:tt]])#사전에서 msg[:tt]를 key로 갖는 value를 answer에 붙이고
            dictionary[msg[:tt + 1]] = num #msg[:tt+1]은 사전에 추가
            num += 1
        msg = msg[tt:] #msg = msg[tt:]로 슬라이싱
    return answer
```

## 3. 회고

- 처음에 문제를 내 맘대로 해석해서 이상하게 풀어서 오류가 났다.
- 구체적인 알고리즘이 나와있는 경우, 그대로 구현할 것!
- 만약

## 4. 참고

https://programmers.co.kr/learn/courses/30/lessons/17684/solution_groups?language=python3
https://hynnjnn.tistory.com/23
