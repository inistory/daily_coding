import sys

#지정한 거리를 기준으로, 공유기를 몇개 설치할 수 있는지
def router_counter(distance, house):
    count = 1
    cur_house = house[0] #시작점
    for i in range(1, N): #집모두를 돈다
        if cur_house + distance <= house[i]: #이전 집에서 해당 거리보다 멀리 떨어진 집이라면
            count += 1 #공유기 설치
            cur_house = house[i] #공유기 설치된 집 갱신
    return count

N, C = map(int, (input().split()))#집, 공유기 갯수
house = [int(sys.stdin.readline()) for _ in range(N)] #집 좌표
house = sorted(house) #이분탐색을 위한 정렬

start=1 #가능한 최소 거리
end = house[-1] - house[0] #가능한 최대거리

while start <= end: #이분탐색
    mid = (start+end) // 2 #가장 인접한 두 공유기 사이의 거리 지정
    if router_counter(mid, house) >= C:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)
