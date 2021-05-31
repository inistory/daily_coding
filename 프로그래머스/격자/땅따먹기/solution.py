def solution(land):
    sum = 0

    for i,lan in enumerate(land):
        max = 0
        pre_max_idx = 0
        for j, la in enumerate(lan):
            if max < la and j!=pre_max_idx:
                max =la
        sum+=max
    return sum