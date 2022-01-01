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
            if len(max_a[3]) < len(a[3]): #재생시간이 가장 긴 음악 반환
                max_a = a
        return max_a[2]
