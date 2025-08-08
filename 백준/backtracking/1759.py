import sys

L, C = map(int, sys.stdin.readline().split())
chars = sorted(sys.stdin.readline().split())  # 입력 두 줄 형식이면 사용, 한 줄이면 적절히 수정

vowels = set('aeiou')
path = []

def dfs(idx, picked, vcnt, ccnt):
    # L개 채웠으면 조건 검사 후 출력
    if picked == L:
        if vcnt >= 1 and ccnt >= 2:
            print(''.join(path))
        return
    # 범위 밖이면 종료
    if idx == C:
        return
    # 가지치기: 남은 개수로 L 못 채우면 컷
    if picked + (C - idx) < L:
        return

    ch = chars[idx]

    # 1) 현재 문자 선택
    path.append(ch)
    if ch in vowels:
        dfs(idx + 1, picked + 1, vcnt + 1, ccnt)
    else:
        dfs(idx + 1, picked + 1, vcnt, ccnt + 1)
    path.pop()

    # 2) 현재 문자 건너뛰기
    dfs(idx + 1, picked, vcnt, ccnt)

dfs(0, 0, 0, 0)
