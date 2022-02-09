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

def play_time(start_time,end_time): #재생시간 계산하는 함수
    start = start_time.split(":")
    end = end_time.split(":")
    play_time = 0
    play_time = (int(end[0]) - int(start[0])) * 60 + int(end[1]) - int(start[1])
    return play_time

#
def make_played_music_code(playtime, code):#재생된 코드 구하기
    if len(code) > playtime: #코드길이 > 시간
        code = code[:playtime]
    else:  #코드길이 < 시간
        #시간(14)  - 주어진 코드길이(7) = 7 -> 코드[:7]
        q,r = divmod(playtime,len(code))
        code = code*q + code[:r]

    return code

def solution(m, musicinfos):
    music_dic = {}
    replaced_code = ""
    time = 0
    for _, music in enumerate(musicinfos):
        info = music.split(",")
        replaced_code = replace_code(info[3])
        time = play_time(info[0],info[1]) #play time 구하기
        music_dic[info[2]] = make_played_music_code(time,replaced_code) #곡이름, 재생된 코드

    answer = {}
    for key,item in music_dic.items():
        if replace_code(m) in item:
            answer[key] = len(item)

    if answer == {}:
        return "(None)"

    elif len(answer.keys()) ==1:
        for key in answer.keys():
            return key
    else:
        return max(answer,key=answer.get)
```

## 3. 어려웠던 점

```python
조건이 일치하는 음악이 여러 개일 때에는 라디오에서 재생된 시간이 제일 긴 음악 제목을 반환한다. 재생된 시간도 같을 경우 먼저 입력된 음악 제목을 반환한다.
조건이 일치하는 음악이 없을 때에는 “(None)”을 반환한다.
```

- 위의 조건들을 초반에 놓치고 다른 테스트 케이스에서 에러가 났었는데, 다음부터는 놓친 조건들이 없는지 확인해야겠다.

- 딕셔너리에서 가장 큰 value를 가진 key 값을 찾을 때는 아래 코드를 사용하면 된다.

  ```python
  max(answer,key=answer.get)
  ```

  get함수는 선언된 dict에서 출력하고자 하는 key가 있으면, 그에 해당하는 value를 출력해줌

- 재생된 악보정보 구할 때 조건 : 코드길이가 재생시간보다 길면, 코드길이를 재생시간만큼 줄이고, 코드길이가 재생시간보다 짧으면 재생시간에 맞춰 반복한다.
