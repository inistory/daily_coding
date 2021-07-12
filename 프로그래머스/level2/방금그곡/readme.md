## 1. 문제 설명

[문제 링크](https://programmers.co.kr/learn/courses/30/lessons/17683)

- 네오가 들은 음악의 정보가 주어질 때, 음악의 제목을 구하기
- 각 음은 1분에 1개씩 재생
- 조건이 일치하는 음악이 여러 개일 때에는 → 재생된 시간이 제일 긴 음악 제목을 반환
- 재생된 시간도 같을 경우 → 먼저 입력된 음악 제목을 반환
- 조건이 일치하는 음악이 없을 때에는 “(None)”을 반환
- 입력
  - m : 네오가 기억한 멜로디를 담은 문자열
  - musicinfos : 방송된 곡의 정보를 담고 있는 배열(음악이 시작한 시각, 끝난 시각, 음악 제목, 악보 정보)
- 출력
  - return : 실제로 들은 음악의 제목

## 2. 코드

```python
def replace_code(str):
    str = str.replace("C#","c")
    str = str.replace("D#","d")
    str = str.replace("E#","e")
    str = str.replace("F#","f")
    str = str.replace("G#","g")
    str = str.replace("A#","a")
    return str


def get_playtime(code):
    playtime = 0
    start_time = code[0].split(':')
    end_time = code[1].split(':')
    playtime = (int(end_time[0]) - int(start_time[0]))*60 + int(end_time[1]) - int(start_time[1])
    return playtime

def make_played_music_code(playtime,code):
    if len(code[3]) > playtime:
        code[3] = code[3][:playtime]
    elif  len(code[3]) <= playtime: #코드길이 < 시간
        #시간(14)  - 주어진 코드길이(7) = 7 -> 코드[:7]
        q,r = divmod(playtime,len(code[3]))
        code[3] = code[3]*q + code[3][:r]

    return code

def solution(m, musicinfos):
    temp = []
    for info in musicinfos:
        code = info.split(',')
        #replace # to char
        m = replace_code(m)
        code[3] = replace_code(code[3])
        #get playtime
        playtime = get_playtime(code)
        temp.append(make_played_music_code(playtime,code)) #make complete music code

    answer = []
    for t in temp:
        if m in t[3]:
            answer.append(t)

    if answer == []:
        return "(None)"
    else:
        max_a = ["","","",""]
        for a in answer:
            print(a)
            if len(max_a[3]) < len(a[3]): #재생시간이 가장 긴 음악 반환
                max_a = a
        return max_a[2]

```

## 3. 어려웠던 점

- C#과 C를 분리하는 것, #이 달린 코드를 다른 문자열로 치환하고 시작했으면 헤메지 않았을 텐데, 그게 문제가 된다는 것을 나중에 캐치하고 코드내에서 예외처리를 하려다가 힘들었다. 결국 초반에 치환하는 것으로 변경

```python
조건이 일치하는 음악이 여러 개일 때에는 라디오에서 재생된 시간이 제일 긴 음악 제목을 반환한다. 재생된 시간도 같을 경우 먼저 입력된 음악 제목을 반환한다.
조건이 일치하는 음악이 없을 때에는 “(None)”을 반환한다.
```

- 위의 조건들을 초반에 놓치고 다른 테스트 케이스에서 에러가 났었는데, 에러가 날 때는 당황하지 말고 놓친 조건들이 없는지 확인해야겠다. 테스트 케이스 추가하는 방법도 배웠다!

- 특정 조건(재생된 시간도 같을 경우 먼저 입력된 음악 제목을 반환한다.)과 같은 경우, 추가적인 수정이 없어도 원래 그렇게 동작하기도 하니 로직을 잘 살펴봐야 한다.

- max_a = ["","","",""] 이렇게 해주지 않고, max_a = [] 라고 하면 IndexError: list index out of range 에러가 뜬다.
