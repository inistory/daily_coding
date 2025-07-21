import sys

input = sys.stdin.readline

# 1. N 입력
N = int(input())

# 2. 10001 크기의 리스트 정의
count = [0] * 10001

# 3. N개의 정수를 리스트의 인덱스로 접근하여 개수 세기
for _ in range(N):
    num = int(input())
    count[num] += 1

# 4. 리스트에 접근해 그 개수만큼 인덱스 출력
for i in range(10001):
    # count[i]이 1 이상이라면
    if count[i] != 0:
        # 그 값만큼 출력
        for _ in range(count[i]):
            print(i)
