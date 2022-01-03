## 1. 문제 설명

[문제 링크](https://programmers.co.kr/learn/courses/30/lessons/60057)

- 입력 :

  - s "aabbaccc" : 문자열

- 출력 :
  - result 7
  - 몇 개 단위로 잘라서 압축했을 때 가장 짧은 길이로 압축이 가능한지 출력

## 2. 코드

solution1.py

```python
def solution(s):
    answer = len(s)
    for i in range(1,int(len(s))+1): #몇개씩 자를지
        pos = 0 #현재위치
        #단위 설정
        length = len(s)
        while pos + i <=len(s):
            unit = s[pos:pos+i]
            pos+=i #i만큼 증가시키기

            #단위가 몇번 등장하는지 찾기
            count =0
            while pos + i  <= len(s):
                if s[pos:pos+i] == unit:
                    count+=1
                    pos +=i
                else:
                    break
            if count>0:
                #감소할 문자열 길이
                length -=i*count
                #증가할 숫자길이 (등장횟수)
                if count<9:
                    length+=1
                elif count < 99:
                    length+=2
                elif count < 999:
                    length+=3
                else: #s의 길이가 1000일 경우
                    length+=4
        answer = min(answer, length)
    return answer


```

## 3. 회고

- 문자열을 건너뛰어가며 자르는 것을 슬라이싱만으로 해보려했었는데 안 되서 결국 현재위치(pos)를 설정하는 방법을 선택했다.
- 그래서 매번 pos+i 해줘서 인덱스 위치를 변경해줘야한다.
- while 문을 사용했다. unit을 설정할 때와 unit이 몇번 등장하는지 찾는 과정 이렇게 두 개의 while문이 있는데, 모두 pos+i이 s의 길이보다 커지면 종료한다.(작거나 같은동안 동작)
- length는 원래 길이에서부터 반복되는 unit의 갯수가 증가하면 i*cnt(몇개단위인지*몇번등장했는지) 만큼 문자열을 감소시킨다.
- 등장횟수가 한 자리수이면 숫자가 하나니까 +1, 두 자리수이면 +2 를 해줘야한다.
- s의 최대 길이가 1000개이다, 만약 a 1000개로 s가 이루어져있다면 ->1000a로 압축한다.
- 따라서 네자리수 일 경우 +4, 그 이상은 등장할 수 없다.
- 단위별로 길이 확정된 후에는 더 작은 길이를 찾아내는 것이 목표이므로, 원래 s의 길이와 비교를 한 후, 작은 것을 선택한다.
- 반복문이 여러개이다보니, pos, length, count, if count>0:, answer = min(answer, length) 등을 어디 놓아야 할지 헷갈렸던 점이 가장 어려웠다.
- 주석처리를 통해 헷갈리지 않도록 표시하고 반복해서 문제를 푸는게 좋을 것 같다.
- https://www.youtube.com/watch?v=SQP6JT4AoAE
