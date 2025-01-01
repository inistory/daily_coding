def solution(s):
    answer = 0
    cnt1, cnt2 = 0,0
    for ss in s:
        if cnt1==cnt2:
            answer+=1
            x=ss
        if x==ss:
            cnt1+=1
        else:
            cnt2+=1
    return answer