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