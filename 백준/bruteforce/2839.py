N = int(input())
count = 0
while N>=0:
    if N%5==0:
        count+=N//5 #몫만큼 추가
        print(count)
        break
    N-=3 #5로 안나누어 떨어지면 3키로 하나빼기
    count+=1

else:
    print(-1)