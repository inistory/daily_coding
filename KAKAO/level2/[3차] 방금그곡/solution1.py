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

'''
- C#과 C를 분리하는 것, #이 달린 코드를 다른 문자열로 치환하고 시작했으면 헤메지 않았을 텐데, 그게 문제가 된다는 것을 나중에 캐치하고 코드내에서 예외처리를 하려다가 힘들었다. 결국 초반에 치환하는 것으로 변경

```python
조건이 일치하는 음악이 여러 개일 때에는 라디오에서 재생된 시간이 제일 긴 음악 제목을 반환한다. 재생된 시간도 같을 경우 먼저 입력된 음악 제목을 반환한다.
조건이 일치하는 음악이 없을 때에는 “(None)”을 반환한다.
```

- 위의 조건들을 초반에 놓치고 다른 테스트 케이스에서 에러가 났었는데, 에러가 날 때는 당황하지 말고 놓친 조건들이 없는지 확인해야겠다. 테스트 케이스 추가하는 방법도 배웠다!

- 특정 조건(재생된 시간도 같을 경우 먼저 입력된 음악 제목을 반환한다.)과 같은 경우, 추가적인 수정이 없어도 원래 그렇게 동작하기도 하니 로직을 잘 살펴봐야 한다.

- max_a = ["","","",""] 이렇게 해주지 않고, max_a = [] 라고 하면 IndexError: list index out of range 에러가 뜬다.
'''