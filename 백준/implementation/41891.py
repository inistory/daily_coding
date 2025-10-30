import sys
from collections import deque
input = sys.stdin.readline

# 4개 톱니바퀴 입력 (각각 길이 8)
arr = [deque(map(int, input().strip())) for _ in range(4)]

K = int(input())

# 맞물림 인덱스
LEFT_IDX, RIGHT_IDX = 6, 2

def apply_rotation(arr, idx, d):
    # idx: 0~3, d: 1(시계) / -1(반시계)
    dirs = [0, 0, 0, 0]
    dirs[idx] = d

    # 왼쪽으로 전파
    for i in range(idx - 1, -1, -1):#왼쪽방향으로 반복문돌기
        if arr[i][RIGHT_IDX] != arr[i + 1][LEFT_IDX]:
            dirs[i] = -dirs[i + 1] #반대로 돌아가게
        else:
            break

    # 오른쪽으로 전파
    for i in range(idx + 1, 4):
        if arr[i - 1][RIGHT_IDX] != arr[i][LEFT_IDX]:
            dirs[i] = -dirs[i - 1]
        else:
            break

    # 한꺼번에 회전 적용
    for i in range(4):
        if dirs[i] == 1:
            arr[i].rotate(1)
        elif dirs[i] == -1:
            arr[i].rotate(-1)

for _ in range(K):
    num, d = map(int, input().split())#회전할 톱니바퀴번호, 방향
    apply_rotation(arr, num - 1, d)

# 점수 계산: 12시가 S(1)면 1,2,4,8 가중치 합산
score = 0
for i in range(4):
    if arr[i][0] == 1:
        score += (1 << i)

print(score)
