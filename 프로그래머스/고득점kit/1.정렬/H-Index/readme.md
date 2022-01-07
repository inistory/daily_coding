## 1. 문제 설명

[문제 링크](https://programmers.co.kr/learn/courses/30/lessons/42747)

- 입력: 어떤 과학자의 논문 n편의 인용된 횟수를 담은 리스트 [3, 0, 6, 1, 5]
- 출력: h번이상 인용된 논문이 h편이상 인용된 경우 중에 h의 최댓값 찾기 3

## 2. 코드

```python
def solution(citations):
    answer = 0
    citations.sort()
    for i in range(1,len(citations)+1): #h후보: 1 ~ 5 각각 h-index가 되는지확인
        min_num = citations[-i]
        if min_num >= i:  #i번째 논문의 인용수가 i보다 크면 i번째 ~ len(citationtion)번째 까지는 모두 hindex 만족
            answer = i #계속 더 큰 값으로 업데이트 됨

    return answer


# [0,1,3,5,6] -> 갯수에 해당
# [1,2,3,4,5] -> h후보 인덱스
```

## 3. 회고

- 문제 이해가 어려웠다.
- 일단 주어진 배열을 오름차순 정렬을 했다. [0,1,3,5,6]
- 먼저 h후보를 만들고, h-index가 되기 위한 조건을 만족하는지 찾아야한다.
- h의 후보들은 1 ~ len(citations) 이기 떄문에 이걸로 for문을 돌린다. [1,2,3,4,5]

- h-index가 되기 위한 조건은 h번이상 인용된 논문이 h편 이상이어야한다는 것이다.

  - citations[-i] : 만약 citations[-1] 이면 6이고 이 값은 i값(1)보다 크다. 1이상의 인용횟수인 논문이 한 개이상인게 확인됐다. 그래서 정답의 후보가 된다.
  - 만약 citations[-2] 는 5이고, 이는 i값인 2보다 크다. 인용횟수가 2이상인게 두 편인게 확인됐다.
  - citations[-3] 은 3이고, 이는 i값인 3과 같다. 인용횟수가 3이상인 논문이 세 편인게 확인됐다.
  - citations[-4] 는 1이고, 이는 i값인 4보다 작기 때문에 h-index의 조건을 만족하지 않는다.

- 포인트는 citations[-i]에서 i가 증가하면서 자동으로 count역할을 하는 것이다. 사전에 배열을 오름차순정렬했기 때문에 가능하다.
- 해설을 보고 겨우 이해하긴 했는데, 이 문제는 다음 번에 다시 풀어봐야겠다.

## 4. References

https://www.youtube.com/watch?v=wW7UTbulKHA
