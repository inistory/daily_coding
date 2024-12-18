def solution(s):
    answer = []
    for ss in list(s.split(' ')):
        temp = ''
        for i in range(len(ss)):
            if i%2==0:
                temp+=ss[i].upper()
            else:
                temp+=ss[i].lower()
        answer.append(temp)
    
    return ' '.join(answer)
    