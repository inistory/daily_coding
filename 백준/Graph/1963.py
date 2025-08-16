import sys
from collections import deque

input = sys.stdin.readline

# 소수 테이블 생성 함수
def get_prime_table():
    is_prime = [False, False] + [True] * (10000 - 2)  # 0,1은 소수 아님
    for i in range(2, int(10000 ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, 10000, i):
                is_prime[j] = False
    return is_prime

is_prime = get_prime_table()

T = int(input())

for _ in range(T):
    start_str, end_str = input().strip().split()
    start = int(start_str)
    end = int(end_str)

    dist = [-1] * 10000   # -1이면 미방문
    dist[start] = 0

    queue = deque([start])

    while queue:
        current = queue.popleft()

        if current == end:
            print(dist[current])
            break

        current_str = str(current)

        for i in range(4):
            for digit in '0123456789':
                if i == 0 and digit == '0':  # 천의 자리 0 금지
                    continue
                if current_str[i] == digit:  # 같은 숫자는 건너뛰기
                    continue

                new_str = current_str[:i] + digit + current_str[i+1:]
                new_num = int(new_str)

                if is_prime[new_num] and dist[new_num] == -1:
                    dist[new_num] = dist[current] + 1
                    queue.append(new_num)
    else:
        print("Impossible")