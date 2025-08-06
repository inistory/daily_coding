def hanoi(n, start, end, temp):
    if n == 1:#원판이 한 개인 경우
        print(start, end)
        return
    hanoi(n - 1, start, temp, end)  # 1단계: n-1개를 보조기둥으로
    print(start, end)              # 2단계: 가장 큰 원판을 목표로
    hanoi(n - 1, temp, end, start)  # 3단계: n-1개를 목표기둥으로

N = int(input()) #옮겨야할 원판개수
print(2**N - 1)  # 최소 이동 횟수
hanoi(N, 1, 3, 2)