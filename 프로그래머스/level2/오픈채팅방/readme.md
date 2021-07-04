## 1. 문제 설명

[문제 링크](https://programmers.co.kr/learn/courses/30/lessons/42888)

- 네오가 들은 음악의 정보가 주어질 때, 음악의 제목을 구하기
- 각 음은 1분에 1개씩 재생
- 조건이 일치하는 음악이 여러 개일 때에는 → 재생된 시간이 제일 긴 음악 제목을 반환
- 재생된 시간도 같을 경우 → 먼저 입력된 음악 제목을 반환
- 조건이 일치하는 음악이 없을 때에는 “(None)”을 반환
- 입력
  - m : 네오가 기억한 멜로디를 담은 문자열
  - musicinfos : 방송된 곡의 정보를 담고 있는 배열(음악이 시작한 시각, 끝난 시각, 음악 제목, 악보 정보)

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

- C#과 C를 분리하는 것
