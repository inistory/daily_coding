def solution(n, m, section):
    count = 0
    while section:
        start = section.pop(0)
        count += 1
        if not section:
            break
        while section[0] <= start+m-1:
            section.pop(0)
            if not section:
                break
        
    return count