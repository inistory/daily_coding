import sys
input = sys.stdin.readline

N = int(input())
meetings = []

for _ in range(N):
    start, end = map(int, input().split())
    meetings.append((start, end))

# 한 회의가 끝나야 다음 회의를 시작할 수 있음
# 끝나는 시간 기준으로 정렬해서 최대한 많은 회의를 할 수 있도록 하기
meetings.sort(key=lambda x: (x[1], x[0]))

count = 0
last_end = 0 #이전회의 종료시간

for start, end in meetings:
    if start >= last_end:
        count += 1
        last_end = end

print(count)
