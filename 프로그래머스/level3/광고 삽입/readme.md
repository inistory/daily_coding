## 1. 문제 설명

[문제 링크](https://programmers.co.kr/learn/courses/30/lessons/72414)

- play_time : 동영상 재생시간 길이
- adv_time : 공익광고의 재생시간 길이
- logs : 시청자들이 해당 동영상을 재생했던 구간 정보
- result : 시청자들의 누적 재생시간이 가장 많이 나오는 곳에 공익광고를 삽입하려 할 떄, 공익광고가 들어갈 시작 시각

## 2. 코드

```python
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

```

## 3. 코드 설명

- 시간을 모두 초로 바꾸어 문제를 푼다.
  - convert() : 시간을 모두 초로 바꿔주는 함수
- 초기화 시에는 log들의 시작지점의 인덱스에 1, 끝나는 지점의 인덱스에 -1을 입력한다.(나머지인덱스는 0으로 초기화)
- 그 후, 전체 playSec 을 for문으로 돌면서 이전값을 현재값에 더하는 행위를 한다.
- 광고가 어디에 들어가야 가장 누적시청구간이 클지 전체 playSec에서 광고 구간을 바꿔가며 count를 하고 max와 비교를 하며 최대시간을 구한다.
- 이 떄에 광고 시간이 1초 움직일 때마다 이전 범위의 첫 인덱스값을 지우고, 새로운 범위의 마지막 인덱스값을 업데이트 해줘야한다.

## 4. 참고

https://www.youtube.com/watch?v=Yr_xHHNsBog
