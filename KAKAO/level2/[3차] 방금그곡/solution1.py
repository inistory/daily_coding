def solution(m, musicinfos):
    temp = []
    for info in musicinfos:
        code = info.split(',')
        start_time = code[0].split(':')
        end_time = code[1].split(':')
        playtime = 0
        #시간 간격 1시간 = 60분, :기준으로 나눠서 앞부분이 같으면 뒤부분 차이가 재생길이
        #앞부분다르면 그 차이*60+ 뒷부분차이
        if start_time[0] ==  end_time[0]:
            play_time = int(end_time[1]) - int(start_time[1])
        else: 
            play_time = (int(end_time[0]) - int(start_time[0]))*60 + int(end_time[1]) - int(start_time[1])
        
        #코드길이와 playtime 비교
        if len(code[3].replace("#","")) > play_time:
            code[3] = code[3][:play_time]
        elif  len(code[3].replace("#","")) <= play_time: #코드길이 < 시간
            #시간(14)  - 주어진 코드길이(7) = 7 -> 코드[:7]
            q,r = divmod(play_time,len(code[3].replace("#","")))
            code[3] = code[3]*q + code[3][:r]
        temp.append(code)

    answer = []
    print(temp)
    for t in temp:
        target_idx = []
        if m in t[3]:
            #range(len(t[3]) = [0,1,2,3]
            target_idx = list(filter(lambda e:t[3][e:e+len(m)]==m, range(len(t[3]))))
            print(target_idx)
            for idx in target_idx:
                
                if idx+len(m) == len(t[3])-1:# #이 없이 끝남
                    answer.append(t)
                    break
                    # return t[2]
                else:
                    if t[3][idx+len(m)] != '#':
                        answer.append(t)
                        break
                        # return t[2]
    if answer == []:
        return "(None)"
    else:
        max_a = ["","","",""]
        for a in answer:
            print(a)
            if len(max_a[3]) < len(a[3]):
                max_a = a
        return max_a[2]
