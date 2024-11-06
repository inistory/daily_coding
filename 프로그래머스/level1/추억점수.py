def solution(name, yearning, photo):
    dic = {}
    for i in range(len(name)):
        dic[name[i]] = yearning[i]
    result = []
    for p in photo:
        answer = 0
        for i in range(len(p)):
            if p[i] in dic:
                answer+=dic[p[i]]
        result.append(answer)
    return result