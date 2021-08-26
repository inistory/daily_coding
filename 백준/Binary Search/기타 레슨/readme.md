## 1. 문제 설명

[문제 링크](https://www.acmicpc.net/problem/2343)

- input :
  - 첫째 줄 : 레슨의 수 N, 블루레이 갯수 M
  - 둘째 줄부터 N개의 줄: 기타 레슨의 길이가 레슨 순서대로 분 단위로(자연수)로 주어진다
- return : 가능한 블루레이 크기중 최소를 출력

## 2. 코드

```python
def add_lesson(mid,lesson_list):
    cnt = 0  # 레코드 갯수 세기
    sum_lesson = 0  # 한 레코드에 들어갈 레슨들의 합
    for i in range(N):
        if sum_lesson + lesson_list[i] > mid:
            cnt += 1
            sum_lesson = 0

        sum_lesson += lesson_list[i]
    else:
        if sum_lesson:
            cnt += 1
    return cnt


N, M = map(int, input().split())  # N: 레슨 수, M: 블루레이 수
lesson_list = list(map(int, input().split()))  # 레슨들

left, right = max(lesson_list), sum(lesson_list)   # 레코드가 가질 수 있는 가장 작은 크기, 레슨을 하나의 레코드에 다 담을 수 있을 때 레코드의 크기는 레슨의 합이다

while left <= right:
    mid = (left + right) // 2 # 레코드 크기 중간값 구하기
    if add_lesson(mid,lesson_list) <= M:  # 레코드 숫자가 모자라면 레코드 크기(mid)를 줄인다.
        right = mid - 1
    elif add_lesson(mid,lesson_list) > M:  # 레코드 숫자가 더 많아지면 레코드 크기(mid)를 늘린다
        left = mid + 1

print(left) # 최소 크기니까 left
```

## 3. 코드 설명

- 먼저 왼쪽, 오른쪽, 중간값을 초기화 합니다.
- 블루레이 크기에 따라서 레슨들의 값을 차례차례 더해서 넣어보고 그 크기를 넘어갈 때마다 블루레이 개수를 +1씩 해줍니다.
- 이제 블루레이의 개수에 따라 크기를 늘릴지 줄일지 정합니다.
  - 블루레이 개수가 부족하다면 right = mid - 1 을 해줘서 블루레이 크기를 줄입니다.
  - 블루레이 개수가 넘어간다면 left = mid + 1 을 해줘서 블루레이 크기를 늘립니다.
- 마지막으로 left 를 출력하면 답이 됩니다.

## 4. 어려웠던 점

- 한 레코드 뿐만 아니라 블루레이 갯수까지 함께 고려하여 코드를 구현하는 방법

## 5. 참고

https://deok2kim.tistory.com/109
