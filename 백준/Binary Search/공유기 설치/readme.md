## 1. 문제 설명

[문제 링크](https://www.acmicpc.net/problem/2110)

- input :
  - 첫째 줄 : 집의 개수 N, 공유기의 개수 C
  - 둘째 줄부터 N개의 줄: 집의 좌표
- return : 첫째 줄에 가장 인접한 두 공유기 사이의 최대 거리

## 2. 코드

```python
import sys
N, C = map(int, (input().split()))
house = [int(sys.stdin.readline()) for _ in range(N)]

#해당 거리를 유지하며 공유기가 몇 개 설치될 수 있는가?
def router_counter(distance):
    count = 1
    cur_house = house[0] #시작점
    for i in range(1, N): #집모두를 돈다
        if cur_house + distance <= house[i]: #이전 집에서 해당 거리보다 멀리 떨어진 집이라면
            count += 1
            cur_house = house[i] #공유기 설치된 집 갱신
    return count

house = sorted(house) #이분탐색을 위한 정렬
start, end = 1, house[-1] - house[0] #1, 첫집과 끝집의 거리

while start <= end: #이분탐색 알고리즘
    mid = (start+end) // 2
    if router_counter(mid) >= C:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)

```

## 3. 코드 설명

- mid에 거리를 설정
- 그 거리를 기준으로 다른 집들에 공유기를 설치한다고 가정할 때, 해당거리보다 멀린 떨어진 집일 경우 공유기 설치 표시를 하고, 그 집과 거리의 합산을 기준으로 나머지 집이 공유기를 설치해야하는지 검사
- router_counter(mid) : 공유기를 설치해야하는 집의 갯수를 반환
- if router_counter(mid) >= C:
  - answer = mid : answer에 mid 거리를 일단 넣어둠 (아직 정답인지는 모름)
  - start = mid + 1 : 설치해야할 갯수보다 공유기를 설치해야하는 집의 갯수가 더 많다면 거리를 늘려준다.
  - start = mid + 1 : 같더라도 더 최대의 거리가 있을 수 있음으로 거리를 늘려본다 -> start가 커지면 start+end//2의 값이 커짐, 즉 거리증가
- else: 해당 거리로 충분한 설치 장소를 찾지 못했다면 거리를 줄여주고
  -start <=end 조건이 맞지않는 경우 종료

## 4. 어려웠던 점

- 이분 탐색 알고리즘
- while 문 종료조건과 문제해결의 상관관계

## 4. 참고

- https://claude-u.tistory.com/448
