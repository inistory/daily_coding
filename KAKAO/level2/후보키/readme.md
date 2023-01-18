## 1. 문제 설명

[문제 링크](https://programmers.co.kr/learn/courses/30/lessons/42890)

- 입력 : 데이터 베이스 정보
- 출력 : 후보키가 몇개 존재하는지

## 2. 코드

```python
from itertools import chain, combinations

#모든 부분집합(열의 쌍)을 구하는 함수
def get_all_subset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s,r) for r in range(len(s)+1))

#부분집합 중에서 유일성을 만족하는 부분집합(열의 쌍)을 구하는 함수
def get_all_unique_subset(relation):
    subset_list = get_all_subset(list(range(0,len(relation[0]))))
    unique_list = []
    for subset in subset_list:
        unique = True
        row_set = set()
        for i in range(len(relation))

```

## 3. 회고

- 비트 연산자를 활용
- 세 가지 파트로 나누어서 프로그램 작성
  - 모든 부분집합을 구하기
  - 부분집합 중에서 유일성을 만족하는 부분집합을 구하기
  - 유일성을 만족하는 부분집합 중에서 최소성을 만족하는 부분집합만을 남기기

## 4. 참고

https://www.youtube.com/watch?v=7f1yXtfbWKY
https://www.youtube.com/watch?v=Rgw0fo6isUM
