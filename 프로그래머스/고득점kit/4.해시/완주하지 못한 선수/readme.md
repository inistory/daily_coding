## 1. 문제 설명

[문제 링크](https://programmers.co.kr/learn/courses/30/lessons/42576)

- participant : 마라톤 경기에 참여한 선수들의 이름이 담긴 배열
- completion : 완주한 선수들의 이름이 담긴 배열
- return : 완주하지 못한 선수의 이름

## 2. 코드

```python
def solution(participant, completion):
    participant.sort()
    completion.sort()

    for i in range(len(completion)) :
        if participant[i] != completion[i] :
            return participant[i]
    return participant[-1]
```

-

## 3. 어려웠던 점

- 정렬을 하지 않고 풀었을 때는 효율성이 좋지 않아서 코드를 수정했다.
