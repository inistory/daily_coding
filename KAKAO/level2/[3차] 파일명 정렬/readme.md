## 1. 문제 설명

[문제 링크](https://programmers.co.kr/learn/courses/30/lessons/17686)

- 입력 : 파일이름들
- 출력 : 문자부분, 숫자부분, 남은 부분으로 나누어서 정렬기준에 맞게 정렬된 파일명 출력

## 2. 코드

solution1.py

```python
from functools import cmp_to_key

def compare(s1,s2):
    head1, number1, tail1 = s1[0], s1[1], s1[2]
    head2, number2, tail2 = s2[0], s2[1], s2[2]

    head1, head2 = head1.upper(), head2.upper() #알바벳 구분 없으니까
    number1, number2 = int(number1), int(number2) #비교를 위해 int화

    if head1 != head2:
        return -1 if head1 < head2 else 1 #만약 head1이 head2보다 작으면 교환(-1)
    else: #head1 == head2
        return number1 - number2 if number1 != number2 else 1 #숫자가 서로 같지 않을 때만 빼기(둘이 같을 때(둘을 서로 빼면 0이니까) 교환이 되어버림을 방지)

def split_fname(filename):
    HEAD = ""
    NUMBER = ""
    TAIL = ""
    i = 0
    while not filename[i].isnumeric():
        i+=1
    HEAD = filename[:i]

    j = i
    while filename[j].isnumeric():
        j+=1
        if j == len(filename): #TAIL이 없는 경우
            NUMBER = filename[i:j]
            return [HEAD, NUMBER, '']

    NUMBER = filename[i:j]
    TAIL = filename[j:]

    return [HEAD, NUMBER,TAIL]


def solution(files):
    answer = []
    filenames  = []
    for file in files: #파일명 하나씩 조회
        filenames.append(split_fname(file))

    filenames.sort(key=cmp_to_key(compare))

    for i, filename in enumerate(filenames):
        filenames[i] = ''.join(filename)
    return filenames
```

## 3. 회고

- 문자열 자르기에서 많이 해맸다. for문보다 while문을 사용하면 쉽게 풀리는 문제였다.

- cmp_to_key란?

  - from functools import cmp_to_key로 선언
  - functools.cmp_to_key(func) 함수는 sorted와 같은 정렬 함수의 key 매개변수에 함수(func)를 전달할 때 사용하는 함수이다.
  - 단, func 함수는 두 개의 인수를 받아들이고, 첫번째 인수를 기준으로 그들을 비교하여, 작으면 음수, 같으면 0, 크면 양수를 반환하는 비교 함수이어야 한다.

- 정렬을 할 때, cmp_to_key를 활용해야한다.

  - from functools import cmp_to_key로 선언
  - cmp_to_key안에는 compare 함수를 넣는다.
  - compare 함수는 비교해서 앞 원소가 더 작으면 -1을 반환해서 서로 교환(위치를 바꿈)하게하고,서로 같으면 0을 반환(교환), 앞 원소가 더 크면 1을 반환(교환하지않음)한다.

- 주의 1) tail이 없는 경우
  - tail이 없는 경우는 예외처리를 해주어야한다. 안하면 런타임 에러가 날 수 있음
- 주의 2) 파일명 원상복귀
  - ''.join(filename) 로 나누어놓은 파일명리스트를 string형태로 바꿔주자

## 4. 참고

https://www.youtube.com/watch?v=IcNPpsG8i2s
https://wikidocs.net/109303
