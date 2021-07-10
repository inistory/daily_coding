## 1. 문제 설명

[문제 링크](https://programmers.co.kr/learn/courses/30/lessons/42577)

- phone_book : 전화번호 부에 적힌 전화번호를 담은 배열
- return : 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false, 그렇지 않으면 true

## 2. 코드

```python
def solution(phone_book):
    phone_book = sorted(phone_book)

    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True
```

## 3. 어려웠던 점

- sort를 하면 2중 for문을 사용할 필요가 없다
