## 1. 문제 설명

[문제 링크](https://www.acmicpc.net/problem/2110)

- input :
  - 첫째 줄 : 집의 개수 N, 공유기의 개수 C
  - 둘째 줄부터 N개의 줄: 집의 좌표
- return : 첫째 줄에 가장 인접한 두 공유기 사이의 최대 거리

## 2. 코드

```python
import sys

#지정한 거리를 기준으로, 공유기를 몇개 설치할 수 있는지
def router_counter(distance, house):
    count = 1
    cur_house = house[0] #시작점
    for i in range(1, N): #집모두를 돈다
        if cur_house + distance <= house[i]: #이전 집에서 해당 거리보다 멀리 떨어진 집이라면
            count += 1 #공유기 설치
            cur_house = house[i] #공유기 설치된 집 갱신
    return count

N, C = map(int, (input().split()))#집, 공유기 갯수
house = [int(sys.stdin.readline()) for _ in range(N)] #집 좌표
house = sorted(house) #이분탐색을 위한 정렬

start=1 #가능한 최소 거리
end = house[-1] - house[0] #가능한 최대거리

while start <= end: #이분탐색
    mid = (start+end) // 2 #가장 인접한 두 공유기 사이의 거리 지정
    if router_counter(mid, house) >= C:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)

```

## 3. 회고

- 문제를 이해하는데 좀 걸렸다.
- "가장 인접합 두 공유기 사이의 거리"의 최댓값을 탐색하는 문제이다.
- mid로 가장 인접한 두 공유기 사이의 거리를 설정한다.
- 그 거리를 기준으로 다른 집들에 공유기를 설치할 때, 해당거리보다 멀린 떨어진 집일 경우 공유기 설치 표시를 하고, 그 집과 거리의 합산을 기준으로 나머지 집이 공유기를 설치해야하는지 검사한다.
- router_counter(mid) : 공유기를 설치해야하는 집의 갯수를 반환
- if router_counter(mid) >= C:
  - answer = mid : answer에 mid 거리를 일단 넣어둠 (아직 정답인지는 모름)
  - start = mid + 1 : 설치해야할 갯수보다 공유기를 설치해야하는 집의 갯수가 더 많다면 거리를 늘려준다.
  - start = mid + 1 : 같더라도 더 최대의 거리가 있을 수 있음으로 거리를 늘려본다 -> start가 커지면 start+end//2의 값이 커짐, 즉 거리증가
- else: 해당 거리로 충분한 설치 장소를 찾지 못했다면 거리를 줄여주고
  -start <=end 조건이 맞지않는 경우 종료
