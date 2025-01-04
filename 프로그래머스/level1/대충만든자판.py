def solution(keymap, targets):
    #키가 len(keymap)개 있는데,
    #타겟문자가 좀 더 앞쪽에 있는거를 선택하고 그것이 몇번째위치해 있는지를 더해주면 됨
    #어디에도 존재하지 않으면 -1
    
    key_dict = {}
    answer = []
    for key in keymap:
        for i, ch in enumerate(key):
            if ch not in key_dict:
                key_dict[ch] = i+1
            else:
                if key_dict[ch] > i+1:
                    key_dict[ch] = i+1
    
    for target in targets:
        count = 0
        for ch in target:
            if ch in key_dict:
                count+=key_dict[ch]
            else:
                count= -1
                break
        answer.append(count)
    return answer
                