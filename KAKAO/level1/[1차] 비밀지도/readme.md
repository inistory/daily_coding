## 1. 문제 설명

[문제 링크](https://programmers.co.kr/learn/courses/30/lessons/17681)

- 입력 :

  - n 5 : 정사각형 변 길이
  - arr1 [9, 20, 28, 18, 11] : 지도1 에 들어가는 숫자
  - arr2 [30, 1, 21, 17, 28] : 지도2 에 들어가는 숫자

- 출력 :
  - ["#####","# # #", "### #", "# ##", "#####"]
  - 지도 1,2를 각각 이진수로 변경 후, 둘 다 0일경우는 공백, 하나라도 1일 경우는 #으로 변경하여 출력

## 2. 코드

solution1.py

```python
def solution(n, arr1, arr2):
    temp1 = []
    temp2 = []
    for i in range(n):
        temp1.append(list(format(arr1[i],'b').zfill(n)))
        temp2.append(list(format(arr2[i],'b').zfill(n)))

    #두 리스트를 비교
    answer = []
    for tmp1, tmp2 in zip(temp1, temp2):
        s = []
        for t1,t2 in zip(tmp1, tmp2):
            if t1 =='0' and t2=='0':
                s.append(" ")
            else:
                s.append("#")
        answer.append("".join(s))
    return answer

```

## 3. 회고

- 이진수로 변경하는 과정에서 bin()함수를 쓰니 b라는 문자가 포함되는 문제가 있었다
- 이를 위해 format(리스트,'b')를 대신 사용했다.
- 이진 수로 변경했을 때, 00001이 되어야할 것이 1로 되어서 zfill(문자열길이)를 통해 앞쪽에 0을 채워주었다.
- zip을 써서 두 이차원 리스트를 동시에 순회했는데, 이 문제의 경우엔 인덱스로 접근하는 방법을 그냥 써도 괜찮을 것 같다.
