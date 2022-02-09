## 1. 문제 설명

[문제 링크](https://programmers.co.kr/learn/courses/30/lessons/42890)

- 입력 : 데이터 베이스 정보
- 출력 : 후보키가 몇개 존재하는지

## 2. 코드

```python
from functools import cmp_to_key
def compare(a,b):
    x = bin(a).count('1')#a에서 비트개수 세기
    y = bin(b).count('1')

    return x - y #오름차순 정렬


def check(relation , rowsize, colsize, subset):
    #튜플이 서로 식별이 되는지 확인
    #1.(두개씩 쌍짓기)
    for a in range(rowsize - 1):
        for b in range(a+1, rowsize):
            #2.서로 구별이 되는지 확인
            isSame = True
            #각각의 속성을 활용해서 튜플이 서로 구별이 되는지 봄
            for k in range(colsize):
                #n번비트는 n번 속성을 나타냄
                #k번째 비트가 켜져있다면 0이 아니고
                #subset에 포암된 속성인지 확인
                if (subset & 1<<k) == 0: #포함된 속성이 아니라면
                    continue
                #여기까지 왔다면 subset에 포함된 속성이기 때문에 튜플간 구별여부 확인
                if relation[a][k] != relation[b][k]:
                    isSame = False
                    break #하나라도 다르면 나머지를 확인할 필요가 없으니까
            #다른속성이 하나도 없다 -> 두개의 튜플이 구분이 안됨 -> 유일성만족못함
            if isSame:
                return False
    #모든 조합에 대해서 다 확인했는데 return 되지않고 for문이 끝났으면 유일성만족
    return True #유일성 확인완료



def solution(relation):
    answer = 0
    rowsize = len(relation)
    colsize = len(relation[0])
    candidates = []

    #전체 부분집합의 갯수만큼 반복, 단, 아무것도 없는 건 필요없으니 제외
    for i in range(1,1 << colsize):
        if check(relation, rowsize,colsize, i):
            candidates.append(i)
    #최소성만족하는지 검사
    #비트가 오름차순으로 정렬됨
    candidates = sorted(candidates,key=cmp_to_key(compare))

    #불필요하게 더 속성을 가진 후보키들을 삭제
    while len(candidates) != 0:
        n = candidates.pop(0)
        answer += 1
        candidates = [x for x in candidates if (n & x) != n ]

    return answer

```

## 3. 어려웠던 점

- 비트 연산자를 활용
- 아직 코드가 이해가 안감

## 4. 참고

https://www.youtube.com/watch?v=7f1yXtfbWKY
