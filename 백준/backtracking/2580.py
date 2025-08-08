import sys
input = sys.stdin.readline

BOARD_SIZE = 9
ALL = 0b1111111110  # 1~9 비트(1<<1 ... 1<<9)만 사용

board = [list(map(int, input().split())) for _ in range(BOARD_SIZE)]

rows = [0] * BOARD_SIZE
cols = [0] * BOARD_SIZE
boxes = [0] * BOARD_SIZE
empties = []

def box_idx(r, c):
    return (r // 3) * 3 + (c // 3)

# 초기 마스크 구성
for r in range(BOARD_SIZE):
    for c in range(BOARD_SIZE):
        v = board[r][c]
        if v == 0:
            empties.append((r, c))
        else:
            bit = 1 << v
            rows[r] |= bit
            cols[c] |= bit
            boxes[box_idx(r, c)] |= bit

def solve():
    if not empties:
        # 정답 출력
        out = []
        for r in range(BOARD_SIZE):
            out.append(" ".join(map(str, board[r])))
        print("\n".join(out))
        sys.exit(0)

    # MRV: 후보가 가장 적은 칸 선택
    best_i = -1
    best_mask = 0
    best_count = 10

    for i, (r, c) in enumerate(empties):
        used = rows[r] | cols[c] | boxes[box_idx(r, c)]
        cand = (~used) & ALL  # 가능한 숫자들의 비트마스크
        if cand == 0:
            return  # 이 분기는 불가능
        # 후보 개수 세기
        cnt = cand.bit_count()
        if cnt < best_count:
            best_count = cnt
            best_mask = cand
            best_i = i
            if cnt == 1:
                break  # 더 볼 필요 없음

    # 선택한 칸을 리스트에서 꺼내서 시도
    r, c = empties.pop(best_i)
    b = box_idx(r, c)
    cand = best_mask

    while cand:
        bit = cand & -cand
        cand -= bit
        v = bit.bit_length() - 1

        # 놓기
        board[r][c] = v
        rows[r] |= bit
        cols[c] |= bit
        boxes[b] |= bit

        solve()

        # 되돌리기
        board[r][c] = 0
        rows[r] ^= bit
        cols[c] ^= bit
        boxes[b] ^= bit

    # 복귀 전에 칸 복원
    empties.insert(best_i, (r, c))

solve()
