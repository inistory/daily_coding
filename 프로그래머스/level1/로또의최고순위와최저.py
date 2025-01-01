def solution(lottos, win_nums):
    correct, zero = 0, 0
    for l in lottos:
        if l in win_nums:
            correct += 1
        if l == 0:
            zero += 1

    # 최소와 최대 순위를 계산
    max_rank = 7 - (correct + zero) if correct + zero >= 2 else 6
    min_rank = 7 - correct if correct >= 2 else 6

    return [max_rank, min_rank]
