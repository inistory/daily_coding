## 1. 문제 설명

[문제 링크](https://www.acmicpc.net/problem/11729)

- input : 첫 번째 장대에 쌓인 원판의 개수 N (1 ≤ N ≤ 20)
- return : 첫째 줄에 옮긴 횟수 K, 두 번째 줄부터 수행 과정을 출력한다. 두 번째 줄부터 K개의 줄에 걸쳐 두 정수 A B를 빈칸을 사이에 두고 출력하는데, 이는 A번째 탑의 가장 위에 있는 원판을 B번째 탑의 가장 위로 옮긴다는 뜻이다.

## 2. 코드

```python
def hanoi(n, start, end) :
    if n == 1 : #원판이 하나일 때
        print(start, end)
        return

    hanoi(n-1, start, 6-start-end) # 1. 맨 아래를 제외한 원반들을 다른 기둥으로 옮긴다
    print(start, end) # 2. 맨 아래 원반을 목적지 기둥으로 옮긴다
    hanoi(n-1, 6-start-end, end) # 다른 기둥에 옮겨놨던 원반들을 목적지 기둥에 얹는다.

n = int(input())
print(2**n-1) #하노이의 탑 최소이동 횟수 공식
hanoi(n, 1, 3)

```

## 3. 어려웠던 점

- 이동 순서를 표현하는 과정이 어려웠다.
