import sys
input = sys.stdin.readline

N, M = map(int, input().split())
seq = []

#정렬된 수열만 만들기
def dfs(start):
    if len(seq) == M:#현재 만든 수열의 길이가 M이 되면 출력하고 종료
        print(" ".join(map(str, seq)))
        return
    for i in range(start, N+1):
        seq.append(i)
        dfs(i)  # start를 그대로 넘김: 중복 허용 + 비내림차순
        seq.pop()

dfs(1)