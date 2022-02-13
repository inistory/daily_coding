def solution(files):
    tmp = []
    head, number, tail = '', '', ''
    
    for file in files:       
        for i in range(len(file)):
            if file[i].isdigit():     # 숫자가 나오면 그 이전은 무조건 HEAD, 이후는 NUMBER, TAIL로 다시 구분
                head = file[:i]
                number = file[i:]
                
                for j in range(len(number)):    # NUMBER와 TAIL 구분 (숫자 안나오면 TAIL)
                    if not number[j].isdigit():
                        tail = number[j:]
                        number = number[:j]
                        break
                        
                tmp.append([head, number, tail])
                head, number, tail = '', '', ''
                break

    tmp = sorted(tmp, key=lambda x:(x[0].lower(), int(x[1])))

    return [''.join(i) for i in tmp]