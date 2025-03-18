#문자열 게임 2

T = int(input())  # 문자열 게임의 수

for _ in range(T):
    W = input().strip()  # 문자열 W
    K = int(input())  # 정수 K

    # 각 문자의 위치를 저장
    char_positions = {}
    for i, char in enumerate(W):
        if char not in char_positions:
            char_positions[char] = []
        char_positions[char].append(i)

    min_length = float('inf')
    max_length = -1

    # 각 문자에 대해 K개를 포함하는 연속 문자열 길이 계산
    for positions in char_positions.values():
        if len(positions) < K:
            continue  # 해당 문자가 K개 미만이면 건너뜀

        # 슬라이딩 윈도우로 최소 및 최대 길이 계산
        for i in range(len(positions) - K + 1):
            window_length = positions[i + K - 1] - positions[i] + 1
            min_length = min(min_length, window_length)
            max_length = max(max_length, window_length)

    # 결과 출력
    if min_length == float('inf') or max_length == -1:
        print(-1)
    else:
        print(min_length, max_length)