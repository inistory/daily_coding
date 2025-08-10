N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

#i<j 쌍에 대해 S[i][j] + S[j][i] 전처리
pair = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(i+1,N):
        pair[i][j] = S[i][j] + S[j][i]
        
visited = [False]*N
visited[0] = True #대칭 깨기:0번은 스타트팀 고정(True가 start팀)
best = float('inf')

#현재 visited 기준으로 두 팀 점수 계산해서 |A-B| 반환.
def evaluate():
    A = B = 0
    for i in range(N):
        vi = visited[i]
        for j in range(i+1, N):
            if vi and visited[j]:
                A += pair[i][j]
            elif (not vi) and (not visited[j]):
                B += pair[i][j]
    return abs(A - B)

#스타트팀 조합을 만들고,팀이 완성되면 evaluate()로 차이를 계산해 best를 갱신
#start:다음에 뽑을 후보 인덱스의 시작점
#picked:지금까지 스타트팀에 들어간 명수
def dfs(start, picked):
    global best #지금까지 본 최소 차이
    if picked == N // 2: #스타트팀이 정원(N/2)찼으면 팀이 완성된 것
        diff = evaluate() #두 팀 내부 시너지 합의 절대차를 계산
        if diff < best:
            best = diff
        return
    if best == 0:#더 줄일 수 없을 때 종료
        return

    for i in range(start, N):#start부터 끝까지 훝으며
        if not visited[i]:#아직 안뽑은 사람을
            visited[i] = True #한명 넣고
            dfs(i + 1, picked + 1) #재귀로 내려감
            visited[i] = False #재귀가 끝나면 되돌려서(백트래킹) 다음후보 시도

dfs(1, 1)  # 0번은 이미 뽑았으니 picked=1, 다음 후보는 1부터
print(best)