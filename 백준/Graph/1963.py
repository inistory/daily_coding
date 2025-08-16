import sys
from collections import deque

input = sys.stdin.readline

# 소수 테이블 생성 함수
#배수를 지우는 행위는 “그 수의 약수가 존재하므로 소수가 아니다”라는 걸 의미
#이걸 반복하면 남는 수는 자기 자신 이외의 약수가 없는 수, 즉 소수만 남음
def get_prime_table():
    is_prime = [False, False] + [True] * (10000 - 2)  # 0,1은 소수 아님, 나머지는 True로 초기화를 해 놓고
    for i in range(2, int(10000 ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, 10000, i): 
                is_prime[j] = False #i가 아직 소수(True)라면, i의 배수들을 모두 False로 변경(에라토스테네스의 체 알고리즘)
    return is_prime

is_prime = get_prime_table()

T = int(input())

for _ in range(T):
    start_str, end_str = input().split()
    start = int(start_str)
    end = int(end_str)

    dist = [-1] * 10000   # -1이면 미방문
    dist[start] = 0

    q = deque([start])

    while q:
        curr = q.popleft()
        curr_str = str(curr)

        if curr == end:
            print(dist[curr])
            break

        for i in range(4):#네자리수
            for digit in '0123456789':#변경가능한 숫자
                if i == 0 and digit == '0':  # 천의 자리 0 금지
                    continue
                if curr_str[i] == digit:  # 같은 숫자는 건너뛰기
                    continue

                new_str = curr_str[:i] + digit + curr_str[i+1:]
                new = int(new_str)

                if is_prime[new] and dist[new] == -1:
                    dist[new] = dist[curr] + 1
                    q.append(new)
    else:
        print("Impossible")