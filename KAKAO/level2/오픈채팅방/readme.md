## 1. 문제 설명

[문제 링크](https://programmers.co.kr/learn/courses/30/lessons/42888)

- 오픈채팅 방에서 회원이 나가고 들어온 정보와 유저아이디가 주어질 때, 특정 유저가 이름을 변경한 것까지 고려하여 문구를 출력
- 딕셔너리를 사용하여 유저 아이디(key), 유저가 사용하는 이름(value) 저장, 변경 시 반영하여 결과 출력 시 사용

## 2. 코드

```python
def solution(record):
    db = {}
    t = ''
    for re in record:
        t = re.split(' ')
        if t[0] != 'Leave':
            db[t[1]] = t[2]

    result = []
    for re in record:
        t = re.split(' ')
        if t[0] == "Enter":
            result.append(db[t[1]]+'님이 들어왔습니다.')
        if t[0] == "Leave":
            result.append(db[t[1]]+'님이 나갔습니다.')
    return result

```

## 3. 어려웠던 점

- 딕셔너리를 사용할 때, 처음에 모든 데이터, 즉 record의 모든 정보를 딕셔너리에 저장하려고 했었는데, 그러지 않고서도 쉽게 풀 수 있었다.
- 처음 풀 때는 for문을 여러개 사용했는데 record에 주어진 문자열을 공배기준으로 나누는 for문, 딕셔너리에 유저아이디와 유저이름 정보를 저장하는 for문을 하나의 for문안에서 진행되도록 수정했다.
