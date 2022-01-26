def solution(s):
    answer = []
    s = s[2:-2] #2},{2,1},{2,1,3},{2,1,3,4
    s = s.split("},{")#['2', '2,1', '2,1,3', '2,1,3,4']
    s.sort(key = len) #['2', '2,1', '2,1,3', '2,1,3,4']
    for ss in s:
        sss = ss.split(',')
        for j in sss:
            if int(j) not in answer: 
                answer.append(int(j))
                print('answer',answer)
    
    return answer