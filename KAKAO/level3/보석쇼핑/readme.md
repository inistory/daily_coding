## 1. 문제 설명

[문제 링크](https://programmers.co.kr/learn/courses/30/lessons/67258)

- 입력
  - gems: 진열된 보석이름
- 출력
  - 모든 보석을 하나 이상 포함하는 가장 짧은 구간을 찾아서 return

## 2. 코드

solution1.py

```python

```

## 3. 회고

- 전체 배열 내 모든 길이를 확인하면서 답을 찾으려 시도했다.
  - O(n^2)로 구현했고, 시간초과가 났다.
  - gems 배열의 크기는 최대 100000 이기 때문에 O(n^2)이상인 탐색 알고리즘으로는 시간 초과가 발생하여 문제를 풀 수 없다.
  - 그러므로 O(n) 으로 탐색할 수 있는 투 포인터 알고리즘을 사용해야 한다.
    - 투포인터 알고리즘?
      - 시작점과 끝점을 이용해 동시에 증가하면서 순차적으로 탐색하는 것

## 4. 참고

https://haeseok.medium.com/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%B3%B4%EC%84%9D%EC%87%BC%ED%95%91-a901de0ce34
https://dev-note-97.tistory.com/70
