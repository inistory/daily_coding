## 1. 문제 설명

[문제 링크](https://programmers.co.kr/learn/courses/30/lessons/42577)

- phone_book : 전화번호 부에 적힌 전화번호를 담은 배열
- return : 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false, 그렇지 않으면 true

## 2. 코드

```python
def solution(phone_book):
    phone_book.sort()
    n = len(phone_book)
    for i in range(n):
        if phone_book[i-1] in phone_book[i][:len(phone_book[i-1])]:
            return False
    return True
```

## 3. 어려웠던 점

- sort를 하면 2중 for문을 사용할 필요가 없다
- if phone_book[i-1] in phone_book[i] 라고만하면 접두사가 아닌 경우도 포함 될 수 있기때문에 [:len(phone_book[i-1])][포함구간의 제한을 두어야한다.
