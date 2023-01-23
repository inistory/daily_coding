# 전기 버스
#https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do
#https://www.youtube.com/watch?v=OjjCSwKUIug


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    #K:한 번에 최대한 이동할 수 있는 정류장 수
    #N: 버스는 0번출발 N번 도착
    #M: 충전기가 설치된 M개의 정류장
    K, N, M = map(int,input().split())
    lst = [0] + list(map(int, input().split())) + [N]

    ans = start = 0
    for i in range(1,M+2):
        #현재 위치 - 이전 위치 > K => 이동불가능
        if lst[i] - lst[i-1] > K:
            ans = 0
            break
        #현재 위치 - 충전시작한지점 > K => 이동불가능
        if lst[i] - start > K:
            start = lst[i-1]
            ans +=1
    print(f'#{test_case} {ans}')
