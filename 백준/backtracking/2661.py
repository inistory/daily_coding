import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline().strip())
ans_found = False

def is_good(s):
    L = len(s)
    # 마지막에 붙인 이후만 검사하면 됨
    for k in range(1, L // 2 + 1): #비교할 앞부분을 봐야하니까 절반만 확인
        if s[L - k:L] == s[L - 2 * k:L - k]:#끝부분을 잘라서 바로 앞부분과 비교
            return False
    return True

def dfs(s):
    global ans_found
    if ans_found:
        return
    if len(s) == N:
        print(s)
        ans_found = True
        return
    for d in "123":
        ns = s + d
        if is_good(ns):
            dfs(ns)
            if ans_found: #제일 빠른 답에서 종료
                return

dfs("")
