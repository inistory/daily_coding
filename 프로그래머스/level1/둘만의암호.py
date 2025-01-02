def solution(s, skip, index):
    
    answer = ''
    skipset = set(skip)
    alphabet = [chr(i) for i in range(ord('a'),ord('z')+1)]
    skip_alphabet = [ch for ch in alphabet if ch not in skipset]
    
    for ch in s:
        cur_index = skip_alphabet.index(ch)
        result_index = (cur_index+index) % len(skip_alphabet)
        answer+=skip_alphabet[result_index]
    
    return answer