def convert(n, base):#n:10진수 base: 진수 k
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]

def solution(n, t, m, p):#진법 n, 미리 구할 숫자의 갯수 t, 게임에 참가하는 인원 m, 튜브의 순서 p
    answer = '' #정답리스트
    tube = ''
    for num in range(m*t):
        answer+=convert(num, n)

    for i in range(p-1, m*t,m):
        tube+= answer[i]

    return tube