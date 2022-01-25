## 1. 문제 설명

[문제 링크](https://programmers.co.kr/learn/courses/30/lessons/92334)

- 입력
  - 유저ID 정보
  - 유저가 신고한 ID 횟수
  - k : k번이상 신고당하면 게시판 이용정지
- 출력 : 유저별로 자신이 신고한 유저 중, 최종 이용정지를 당한 유저의 명수를 세서 리스트 형태로 return

## 2. 코드

solution1.py

```python
def solution(id_list, report, k):
    db = {name:[] for i, name in enumerate(id_list)}
    reports = {name:0 for i, name in enumerate(id_list)}

    for re in set(report):
        user = re.split(" ")[0]
        reported_user = re.split(" ")[1]
        db[user].append(reported_user)
        reports[reported_user] +=1

    answer = [0 for _ in range(len(id_list))]
    for key, values in db.items():
        for value in values:
            if reports[value] >=k:
                answer[id_list.index(key)] += 1
    return answer
```

## 3. 회고

- 한 유저를 여러 번 신고할 경우, 동일한 유저에 대한 신고 횟수는 1회로 처리해야한다.
- 신고된 횟수부분에서 report 목록자체를 set()해주면되는데, if문으로 이미 한 번 신고한 적이 있는 유저인지를 검사했었다가 수정했어서 수정했다.
- 딕셔너리를 사용할 때, value값을 리스트로 하고 여러개의 값을 추가하고 싶을 때는 초기화 시에 지정해주면 편하다.
