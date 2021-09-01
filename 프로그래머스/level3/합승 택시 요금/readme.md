## 1. 문제 설명

[문제 링크](https://programmers.co.kr/learn/courses/30/lessons/72412)

- n: 지점의 개수
- s: 출발지점
- a: A의 도착지점
- b: B의 도착지점
- fares: 특정 두 지점을 오갈 때 발생하는 택시 요금
- result : A, B 두 사람이 s에서 출발해서 각각의 도착 지점까지 택시를 타고 간다고 가정할 때, 최저 예상 택시요금 return

## 2. 코드

```python
INF = 40000000
def floyd(dist, n):
    for k in range(n): #경유지노드
        for i in range(n): #출발점
            for j in range(n): #도착점
                if dist[i][k] + dist[k][j] < dist[i][j]: #i에서 j로 가는데 k를 경유
                    dist[i][j] = dist[i][k] + dist[k][j]

def solution(n,s,a,b,fares):
    dist = [[INF for _ in range(n)]for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0

    for edge in fares:
        dist[edge[0]-1][edge[1]-1] = edge[2] #인덱스를 0부터 사용하기 위해서 1을 빼서 사용, 비용을 넣는다
        dist[edge[1]-1][edge[0]-1] = edge[2] #양방향


    floyd(dist,n)
    s-=1
    a-=1
    b-=1
    answer = INF
    for k in range(n):
        answer = min(answer,dist[s][k] + dist[k][a] + dist[k][b])
    return answer

```

## 3. 코드 설명

- 2차원 배열 dist를 선언하고 최대비용으로 초기화를 시킨다. (INF는 지점갯수가 200이하, 요금이 10만 이하이므로 이를 곱한 값보다 크게만 설정하면 됨)
- 양방향으로 비용 정보를 dist에 초기화해준다.
- floyd(dist, n) 함수
  - A,B가 각각 가는 비용과 특정 지점을 거쳐서 합승하는 비용을 비교해서 더 작은 비용으로 업데이트 해준다. -> 시작지점과 끝지점을 알 떄, 최소의 비용을 계산
- s,a,b 인덱스를 -1해주어 코드에 맞게 바꿔주고,
- for문으로 전체 지점만큼 돌려서 어느지점을 거쳐서 도착지에 가는것이 최소비용인지 찾는다.

## 4. 어려웠던 점

- 가중치 그래프를 어떻게 표현할 것인가
- 최저요금을 어떻게 계산할것인가

## 5. 참고

https://www.youtube.com/watch?v=2iMJclnfQfU
