## 1. 문제 설명

[문제 링크](https://programmers.co.kr/learn/courses/30/lessons/43165)

- 리스트로 수가 주어질 때, + 또는 - 연산을 하여 특정 타겟 넘버가 구해지는 경우의 수를 구한다.
- 리스트에 있는 수들의 +,- 연산 한 모든 경우의 수를 탐색하고, 타겟넘버와 일치하는 결과가 나왔을 때 개수를 센다.

## 2. 코드

```python
answer = 0
def dfs(numbers, target, length, i):
    global answer
    if i == len(numbers): #인덱스 i가 numbers의 길이인 length와 같다면
        if (sum(numbers)) == target: #numbers의 값이 target과 같은지 확인하고
            answer += 1 #같다면 answer의 값을 1 증가킨다.
            return
    else:
        dfs(numbers, target, length, i+1) #그렇지 않다면, dfs(numbers, target, length, i+1)을 호출한 뒤
        #numbers[i]의 값에 -1을 곱한 채로 dfs(numbers,target, length, i+1)을 호출한다.
        numbers[i] *= -1
        dfs(numbers, target, length, i+1)


def solution(numbers, target):
    global answer
    length = len(numbers)
    dfs(numbers, target, length, 0)#dfs(numbers, target, length, 0)을 호출한다.

    return answer
```

## 3. 어려웠던 점

- dfs, bfs 유형의 문제였는데 이를 활용해야된다는 생각에만 꽂혀서 정작 문제를 어떻게 풀어야하는지 생각해내는 데 어려움을 겪었다.
