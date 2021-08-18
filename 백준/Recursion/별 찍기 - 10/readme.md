## 1. 문제 설명

[문제 링크](https://www.acmicpc.net/problem/2447)

- input : N, N은 3의 거듭제곱
- return :

## 2. 코드

```python
N = int(input())
stars = [[0 for i in range(N)] for i in range(N)] #별 존재여부 저장

def fill_star(N, x, y) :
    if N ==1: #종료 조건
        stars[y][x] = '*'
    else:
        next_size = N //3
        for dy in range(3):
            for dx in range(3):
                if dy!=1 or dx!=1: #stars[1][1]에는 항상 별이 있어야함
                    fill_star(next_size, x + next_size*dx, y + next_size*dy) #좌측상단좌표전달


fill_star(N, 0,0)

for row in stars:
    for col in row:
        if col == '*':
            print("*", end="")
        else:
            print(" ", end="")
    print("")

```

## 3. 어려웠던 점

- 재귀를 어떻게 사용해서 풀어야할지 어려웠다.
- 사이즈가 1이 들어오면 해당 좌쵸를 별로 채우고, 사이즈가 1이 아니면 8칸의 서로 다른 좌측 상단 좌표와 1/3한 사이즈의 함수를 재귀호출한다.

## 4. 참고

https://blog.naver.com/PostView.nhn?blogId=repeater1384&logNo=222090302711
