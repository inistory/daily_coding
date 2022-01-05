## 1. 문제 설명

[문제 링크](https://programmers.co.kr/learn/courses/30/lessons/81301)

- 입력 : "one4seveneight"
- 출력 : 1478

## 2. 코드

solution1.py

```python
num_dic = {'zero':'0','one':'1', 'two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}

def solution(S):
    value_list = num_dic.values()
    result = []
    temp = ''
    for i,s in enumerate(S):
        #만약 숫자가 나오면
        if s in value_list:
            result.append(s) #숫자를 append
        #문자가 나오면
        else:
            temp +=s #문자가 존재하면 임시 문자열에 계속 붙이다가
            if temp in num_dic: #임시문자열 중 num_dic의 key에 같은게 있으면
                result.append(num_dic[temp]) #value를 append
                temp = '' #temp를 초기화

    return int(''.join(result)) #리스트 -> 문자열 -> 숫자

```

solution2.py

```python
num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)
```

solution3.py

```python
def solution(S):
    num_dic = {'zero':'0','one':'1', 'two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    value_list = num_dic.values()
    result = ''
    temp = ''
    for i,s in enumerate(S):
        #만약 숫자가 나오면 숫자를 append
        if s in value_list:
            result+=s
        #문자가 나오면
        else:
            temp +=s #key에 문자가 존재하면 임시 문자열에 계속 붙이다가
            if temp in num_dic: #num_dic의 key에 만들어진 임시문자열과 같은게 있으면
                result+=num_dic[temp]#value를 result에 붙임
                temp = '' #temp를 초기화

    return int(result)
```

## 3. 회고

- 다른 코드를 보니 불필요한 변수를 많이 쓴 것 같다.
- 리스트를 문자열로 변경하는 ''.join(리스트) 는 기억해두자
- 딕셔너리에 특정 문자열이 존재하는지 확인할 때는 'for '문자열' in 딕셔너리:'를 쓰면되는데, 문자열이 key에 존재하는지만 알려주기 때문에 딕셔너리의 key와 value를 잘 정하는게 중요했다.
- 하지만 이 모든 건 replace 를 쓰면 아주 간단하게 풀린다...
- num_dic.items()는 아래와 같이 Key와 Value의 쌍을 튜플로 묶은 값을 리스트형태로 돌려준다. key, value 값이 둘 다 존재하는지 확인 가능
  ```python
  dict_items([('zero', '0'), ('one', '1'), ('two', '2'), ('three', '3'), ('four', '4'), ('five', '5'), ('six', '6'), ('seven', '7'), ('eight', '8'), ('nine', '9')])
  ```
- 딕셔너리.keys(), .values(), .items() 들은 모두 리스트를 돌려준다는 것을 기억하자
- solution3.py: 문제를 다시 한 번 풀다가 solution1.py의 코드를 수정했다. reulst = [] 처럼 굳이 리스트를 쓰지않고, reulst = '' 이렇게 처음부터 문자열을 사용하면 더 편하다.
