## 1. 문제 설명

[문제 링크](https://programmers.co.kr/learn/courses/30/lessons/92335?language=python3)

- 입력

  - k: k진수
  - n: 양의 정수

- 출력 : 소수의 개수

## 2. 코드

```python
import math
def convert(n, base):#n:10진수 base: 진수 k
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]

def solution(n, k):
    n = convert(n,k)
    count = 0
    check = True
    for num in n.split('0'):
        if num != '' and num != '1': #빈값이 아니고 1이 아닐 때
            num = int(num)
            #소수인지 검사
            for i in range(2,int(math.sqrt(num))+1):
                if num % i == 0: #나누어떨어지는 수가 있으면
                    check = False #소수가 아님
                    break
            if check: #check가 True라면
                count +=1 #소수니까 +1
    return count
```

## 3. 회고

- 10진수를 k진수로 변환한 후, 조건에 맞는 소수의 개수를 찾아서 문제를 해결했다.

- 10진수를 k진수로 변환하기

  - 재귀함수를 통해 구현이 가능하다
  - 몫이 0이 될 때까지 나머지를 구해야하며 이 과정에서 나온 나머지들을 역순으로 결합해야한다.

- 소수구하기
  - for num in n.split('0')
    - 0을 기준으로 잘라서 숫자들이 소수인지 검사
    - 빈문자열이 나올 수도 있으므로 조건문을 통해 제외시키기 :if num != '
    - 1이면 소수가 아니므로 애초에 count 대상에서 제외 : num != '1'
  - 소수인지 검사
    - range(2, n + 1) 로 하자 시간 초과
    - 약수의 특징을 이용해서 반복문의 횟수를 줄여주는 것이 가능
      - range(2,int(math.sqrt(num))+1) 로 변경
      - 범위 2 ~ N에서 N의 제곱근값보다 작은 부분들에 대한 처리가 끝나면, 제곱근값보다 큰 부분의 값 또한 처리가 된다는 말

## 4. 참고

https://seongonion.tistory.com/43
https://codingdojang.com/scode/458
