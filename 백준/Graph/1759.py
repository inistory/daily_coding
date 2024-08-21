# 암호 만들기

L, C = map(int, input().split())
arr = list(input().split())

def dfs(idx, sentence):
    if len(sentence) == L:
        # 자음 모음 검사
        j = 0
        m = 0
        for s in sentence:
            if s in ['a', 'e', 'i', 'o', 'u']:
                m += 1
            else:
                j += 1
        if m >= 1 and j >= 2:
            print(''.join(sentence))
        return

    for i in range(idx, C):
        dfs(i + 1, sentence + [arr[i]])

arr.sort()
dfs(0, [])