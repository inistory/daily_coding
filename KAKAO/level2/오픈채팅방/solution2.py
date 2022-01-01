def solution(record):
    db = {}
    t = ''
    for re in record:
        t = re.split(' ')
        if t[0] != 'Leave': 
            db[t[1]] = t[2]
    
    result = []
    for re in record:
        t = re.split(' ')
        if t[0] == "Enter":
            result.append(db[t[1]]+'님이 들어왔습니다.')
        if t[0] == "Leave":
            result.append(db[t[1]]+'님이 나갔습니다.')
    return result
