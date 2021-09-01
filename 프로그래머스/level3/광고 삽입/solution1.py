def convert(time):
    h, m ,s = time.split(":")
    return int(h) * 60 * 60 + int(m)*60 + int(s)

def solution(play_time, adv_time, logs):
    playSec = convert(play_time)
    advSec = convert(adv_time)
    
    
    totalSec = [0 for _ in range(playSec + 1)] #0으로 초기화, 인덱스는 하나더 쓰기
    
    for log in logs:
        slog, elog  =log.split("-")
        start = convert(slog)
        end = convert(elog)
        
        totalSec[start] +=1
        totalSec[end]-=1
        
    for i in range(1, playSec):
        totalSec[i] += totalSec[i-1] #이전값으를 현재값과 더함
        
    currSum = sum(totalSec[:advSec]) #누적시청시간 초기화
    
    maxSum = currSum
    maxIdx = 0
    for i in range(advSec, playSec):#최소 누적시청시간구하기
        currSum = currSum + totalSec[i] - totalSec[i-advSec] #위치변경 후 값을 새롭게 반영
        if currSum > maxSum:
            maxSum = currSum
            maxIdx = i-advSec + 1 #빼준거 바로 오른쪽부터 시작
            
    answer = '%02d:%02d:%02d' %(maxIdx/3600,maxIdx/60%60,maxIdx%60)
    return answer
