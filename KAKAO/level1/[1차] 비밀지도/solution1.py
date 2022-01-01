def solution(n, arr1, arr2):
    temp1 = []
    temp2 = []
    for i in range(n):
        temp1.append(list(format(arr1[i],'b').zfill(n)))
        temp2.append(list(format(arr2[i],'b').zfill(n)))
        
    #두 리스트를 비교
    answer = []
    for tmp1, tmp2 in zip(temp1, temp2):
        s = []
        for t1,t2 in zip(tmp1, tmp2):
            if t1 =='0' and t2=='0':
                s.append(" ")
            else:
                s.append("#")
        answer.append("".join(s))
    return answer