## 1. 문제 설명

[문제 링크](https://programmers.co.kr/learn/courses/30/lessons/92341)

- 입력
  - fees: 주차 요금을 나타내는 정수 배열(기본 시간, 기본 요금, 단위시간, 단위 요금)
  - records : 자동차의 입/출차 내역을 나타내는 문자열 배열
- 출력
  - 차량 번호가 작은 자동차부터 청구할 주차 요금을 차례대로 정수 배열에 담아서 return

## 2. 코드

solution1.py

```python
import math

def time_to_minutes(date):
    h, m = map(int, date.split(':'))
    return h*60 + m

def solution(fees, records):
    answer = []

    # 기본 시간, 기본 요금, 단위 시간, 단위 요금 순
    dt, df, ut, uf = fees

    dic = dict()

    for r in records:
        time, car, inout = r.split()
        car = int(car)

        if car in dic: #차별로 주차시간(분단위), inout을 저장
            dic[car].append([time_to_minutes(time), inout])
        else:
            dic[car] = [[time_to_minutes(time), inout]]

    rList = sorted(dic.items()) #key를 기준으로 딕셔너리를 오름차순 정렬해서 리스트로 반환

    for r in rList:
        t = 0

        for rr in r[1]: #item들 확인
            if rr[1] == "IN": #inout가 IN이면
                t -= rr[0] #시간 빼기
            else: #OUT 이면
                t += rr[0] #시간 더하기

        if r[1][-1][1] == "IN": #마지막에 출차 내역이 없는 경우
            t += time_to_minutes('23:59') #출차시간을 23:59으로 간주

        if t <= dt: #기본시간보다 작으면 기본요금을 추가
            answer.append(df)
        else: #기본 시간이상이면
            answer.append(df + math.ceil((t-dt) / ut) * uf)

    return answer
```

## 3. 회고

- 누적시간 계산시, 두 번 이상 주차하는 경우를 생각하지 않음, 알고리즘 구현 전에 예외 케이스 꼭 생각하기

  - 자동차별로 [IN, OUT, 내야할 요금]을 딕셔너리에 정리하고 풀었는데, 두 번 이상 주차하는 경우, IN, OUT 시간이 하나이상 있을 수 있다는걸 나중에 깨달았다. 나는 이전 정보에 새로운 정보를 덮어씌우며 풀고 있었다.
  - 해결 방법 : 어떤 차가 두 번 이상 주차하는 경우 리스트 안에 정보를 추가
    - {5961: [[334, 'IN'], [479, 'OUT'], [1379, 'IN'], [1380, 'OUT']], 0: [[360, 'IN'], [394, 'OUT'], [1139, 'IN']], 148: [[479, 'IN'], [1149, 'OUT']]}

- dictionary의 key로 차 번호를 넣기 전,미리 int()를 씌워줬다 : 차 번호 기준으로 오름차순 정렬 할 때를 위해

  - 나중에 최종 출력에서도 차번호가 빠른 순서대로 "주차요금"만 출력하면되니까 굳이 차 번호를 원상복귀 시킬 필요가 없다.

- 딕셔너리를 key 기준으로 오름차순 정렬하기 : rList = sorted(dic.items())

  - key기준으로 딕셔너리를 오름차순 정렬한 후 리스트로 반환됨

- 동일한 차량의 IN, OUT 때의 시간을 추적해 둘의 시간차를 구하기 보다 각 시간을 분으로 바꾼 시간을 절대적인 시간으로 보고, IN이 나오면 time에서 빼고, 나가면 time에 더하는 방식을 취한다.

## 4. 참고

https://velog.io/@minnseong/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%A3%BC%EC%B0%A8-%EC%9A%94%EA%B8%88-%EA%B3%84%EC%82%B0
