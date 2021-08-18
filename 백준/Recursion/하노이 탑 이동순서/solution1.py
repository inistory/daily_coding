def hanoi(n, start, end) :
    if n == 1 : #원판이 하나일 때
        print(start, end)
        return

    hanoi(n-1, start, 6-start-end) # 1. 맨 아래를 제외한 원반들을 다른 기둥으로 옮긴다
    print(start, end) # 2. 맨 아래 원반을 목적지 기둥으로 옮긴다
    hanoi(n-1, 6-start-end, end) # 다른 기둥에 옮겨놨던 원반들을 목적지 기둥에 얹는다.

n = int(input())
print(2**n-1) #하노이의 탑 최소이동 횟수 공식
hanoi(n, 1, 3)