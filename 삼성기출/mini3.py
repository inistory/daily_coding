# 예: 가장 가까운 대상 중 "거리 → 행↑ → 열↑" 우선
cands = [(dist[r][c], r, c) for r in range(n) for c in range(m)
         if is_target(r,c) and dist[r][c] != -1]
if cands:
    cands.sort()              # 파이썬 튜플은 사전식 비교
    best_dist, br, bc = cands[0]

