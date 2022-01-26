## 1. 문제 설명

[문제 링크](https://programmers.co.kr/learn/courses/30/lessons/64065)

- 입력
  - 부분 집합
- 출력 : 튜플

## 2. 코드

solution1.py

```python
def solution(s):
    answer = []
    s = s[2:-2] #2},{2,1},{2,1,3},{2,1,3,4
    s = s.split("},{")#['2', '2,1', '2,1,3', '2,1,3,4']
    s.sort(key = len) #['2', '2,1', '2,1,3', '2,1,3,4']
    for ss in s:
        sss = ss.split(',')
        for j in sss:
            if int(j) not in answer:
                answer.append(int(j))
                print('answer',answer)

    return answer
```

## 3. 회고

- 문제 이해가 어려웠다.
- 예시를 보고 규칙성을 찾고 풀었다.
- 예시를 보면 s에서 여러번 나온 숫자가 출력에서 앞자리를 차지한다.
- 가장 많이 등장하려면 길이가 작은 집합에도 포함되어 있어야한다. 그래서 길이가 짧은 것부터 긴 순으로 정렬한 후, 먼저나온 순으로 answer에 담고
- 이 후에는 answer에 없는 것만 담으면 된다.
