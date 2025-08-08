import sys
input = sys.stdin.readline

N, S = map(int, input().split())           # N: 원소 개수, S: 목표 합
arr = list(map(int, input().split()))      # 수열

ans = 0                                    # 경우의 수 카운트

def dfs(i, cur_sum):
    """
    i: 현재 보고 있는 인덱스
    cur_sum: 지금까지 선택한 원소들의 합
    """
    global ans
    # 1) 모든 원소를 다 본 경우
    if i == N:
        if cur_sum == S:
            ans += 1
        return

    # 2) i번째 원소를 선택하는 경우
    dfs(i + 1, cur_sum + arr[i])

    # 3) i번째 원소를 선택하지 않는 경우
    dfs(i + 1, cur_sum)

# 탐색 시작
dfs(0, 0)

# 공집합 제거: 아무것도 선택 안 한 경우도 cur_sum == S가 될 수 있으니 빼줌
if S == 0:
    ans -= 1

print(ans)
