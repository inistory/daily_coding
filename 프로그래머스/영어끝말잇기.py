def solution(n, words):
    current_word = [words[0]]
    # print(current_word)
    pre_word = words[0]
    for i in range(1,len(words)): 
        #끝말잇기 규칙위반
        if pre_word[-1] != words[i][0]:
            return [(i % n)+1, (i//n)+1]
        #이미 등장한 단어
        elif words[i] in current_word:
            return [(i % n)+1, (i//n)+1]
        else:
            current_word.append(words[i])
            pre_word = words[i]
            
    return [0,0]