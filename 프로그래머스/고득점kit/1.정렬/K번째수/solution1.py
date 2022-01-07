def solution(array, commands):
    answer = []
    for index, com in enumerate(commands):
        i,j,k = com[0],com[1],com[2]
        temp = sorted(array[i-1:j])
        answer.append(temp[k-1])
    return answer
    