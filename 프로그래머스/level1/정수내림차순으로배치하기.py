def solution(n):
    #str->list->str->int
    return int(''.join(sorted(list(str(n)),reverse=True)))