## 1. 문제 설명

[문제 링크](https://programmers.co.kr/learn/courses/30/lessons/42578)

- clothes : 스파이가 가진 의상들이 담긴 2차원 배열, 각 행은 [의상의 이름, 의상의 종류]
- return : 서로 다른 옷의 조합의 수
- 옷 카테고리별로 딕셔너리를 만들어서 갯수를 세고, 각 카테고리별 장착하지 않은 경우까지 포함하여 조합을 계산하고 아무 것도 장착하지 않은 경우를 뺀다.

## 2. 코드

```python
def solution(clothes):
    answer = {}
    cnt = 1
    for cloth in clothes:
        if cloth[1] in answer:
            answer[cloth[1]] += 1
        else:
            answer[cloth[1]] = 1

    for i in answer.values():
        cnt *= (i+1) #각 카테고리별로 장착하지 않은 경우의 수를 포함하면 +1
    return cnt - 1 #아무것도 장착하지 않은 경우 빼기
```

## 3. 어려웠던 점

- 아무 것도 장착하지 않을 경우를 빼야한다.
