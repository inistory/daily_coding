## 1. 문제 설명

[문제 링크](https://programmers.co.kr/learn/courses/30/lessons/17687?language=python3)

- 입력

  - 진법 n, 미리 구할 숫자의 갯수 t, 게임에 참가하는 인원 m, 튜브의 순서 p

- 출력
  - 튜브가 말해야 하는 숫자 t개를 공백 없이 차례대로 나타낸 문자열. 단, 10~15는 각각 대문자 A~F로 출력

## 2. 코드

```python
def convert(n, base):#n:10진수 base: 진수 k
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]

def solution(n, t, m, p):#진법 n, 미리 구할 숫자의 갯수 t, 게임에 참가하는 인원 m, 튜브의 순서 p
    answer = '' #정답리스트
    tube = ''
    for num in range(m*t):
        answer+=convert(num, n)

    for i in range(p-1, m*t,m):
        tube+= answer[i]

    return tube
```

## 3. 회고

- 10진수를 k진수로 변환하기

  - 재귀함수를 통해 구현이 가능하다
  - 몫이 0이 될 때까지 나머지를 구해야하며 이 과정에서 나온 나머지들을 역순으로 결합해야한다.

- 참가인원\*튜브가 말해야하는 숫자 갯수만큼 숫자(answer)를 구하고
- p-1(인덱스로 조회하기 위해) 부터 m\*t까지 m씩 건너뛰면서 튜브의 값을 조회하여 tube에 붙여줌

## 4. 참고

https://codingdojang.com/scode/458
