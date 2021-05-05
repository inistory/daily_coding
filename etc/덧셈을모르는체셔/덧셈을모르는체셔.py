N = list(input())
cnt = 0

for i in range(len(N)) :
    if int(N[i]) == 0 : #N[i]가 0이여서 10의 자리로 바뀐다면
        cnt += int(N[i-1])*10 #10의 자리 숫자니까 N[i-1]* 10을 더하기
        cnt -= int(N[i-1]) # N[i-1]이 일의 자리라고 생각했을 때 더해준 것을 빼기
        
    cnt += int(N[i]) # 일의 자리 수로 보고 더해주는 것이 기본
print(cnt)
