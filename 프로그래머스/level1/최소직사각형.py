def solution(sizes):
    #가로세로길이를 내림차순 정렬
    #가로에서 제일큰거, 세로에서 제일큰거를 지갑크기로
    
    sorted_sizes = [sorted(size,reverse=True) for size in sizes]
    a = max(ss[0] for ss in sorted_sizes)
    b = max(ss[1] for ss in sorted_sizes)
    
    return a*b
        