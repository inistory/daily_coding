## 1. 문제 설명

[문제 링크](https://programmers.co.kr/learn/courses/30/lessons/42748)

- 입력 : 리스트, 명령(i,j,k)
- 출력 : 리스트를 i번째수부터 j번째 수까지 자른다음, k번째 수를 출력한다., 명령별로 하나씩 리스트에 넣어서 출력

## 2. 코드

solution1.py

```python
def solution(array, commands):
    answer = []
    for index, com in enumerate(commands):
        i,j,k = com[0],com[1],com[2]
        temp = sorted(array[i-1:j])
        answer.append(temp[k-1])
    return answer
```

## 3. 회고

- 제공된 수(commend)보다 하나 적게해야 인덱스와 같아진다.
- 슬라이싱할 때는 i부터 ~ j까지 이면 -> array[i-1:j]이다.
- 마지막 수 전까지 슬라이싱하므로, 뒤에 있는 수는 -1할 필요가 없다.
