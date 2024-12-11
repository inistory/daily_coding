def solution(s):
    s = sorted(list(s),reverse=True)
    answer = ''.join(s)
    return answer