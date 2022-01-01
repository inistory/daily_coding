## 1. 문제 설명

[문제 링크](https://programmers.co.kr/learn/courses/30/lessons/42889)

- 입력 : 5, [2, 1, 2, 6, 2, 4, 3, 3]
- 출력 : [3,4,2,1,5] 실패율이 높은 스테이지순으로 출력

## 2. 코드

å
solution1.py

```python
def fail_percent(target_stage, stages):
    check = 0 #처음 등장하는지 확인
    denominator = 0 #분모값
    numerator = 0 #분자값
    for i,number in enumerate(stages):
        if number == target_stage: #타겟 스테이지의 값과 같은 값이 나오고
            if check==0: #이전에 나온적이 없다면
                denominator = len(stages[i:]) #해당 값 이후로 몇 개가 있는지 확인
                check+=1
                numerator+=1
            else:
                numerator+=1

    if denominator !=0:
        return count / denominator
    else:
        return 0

def solution(N, stages):
    answer = []
    stages.sort() #스테이지를 오름차순 정렬
    storage = {} #각 스테이지별 실패율을 저장할 딕셔너리
    for i in range(N):
        #스테이지(key)별 실패율(value)을 저장
        storage[i+1] = fail_percent(i+1,stages)

    #value 기준으로 key를 내림차순 정렬
    answer = sorted(storage, key= lambda x : storage[x], reverse=True)
    return answer

```

## 3. 회고

- value 기준으로 key를 내림차순 정렬하는 코드를 찾아봤다.
- 바로 리스트를 반환해주어 나중에도 사용하기 유용할 것 같다.
