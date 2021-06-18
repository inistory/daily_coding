def solution(str1, str2):
    strings = []
    for string in [str1,str2]:
        conv = string.lower() 
        convs = {}
        for i in range(0, len(conv)-1):
            word = conv[i:i+2]
            if word.isalpha(): #알파벳이면
                convs[word] = convs.get(word,0)+1 #word라는 key값 있으면 그 값을 받아와서 그 값에 +1, 없으면 0을 넣어줌
        strings.append(convs)
        
        
    str1, str2 = strings
    intersection = [] #교집합
    for s1 in str1:
        if s1 in str2:
            intersection+=[s1 for _ in range(min(str1[s1],str2[s1]))]
    
    union = [] #합집합
    jaccard_keys = list(str1.keys())+list(str2.keys())
    
    for j in set(jaccard_keys): 
        #max(str1[j],str2[j])은 해당 키워드가 한쪽에서없으면 에러가 나서 없는 경우를 0으로 채워주는 코드로 대체    
        union += [j for _ in range(max(str1.get(j,0),str2.get(j,0)))] 
    
    n = len(intersection) / len(union) if len(union)!=0 else 1
    return int(n * 65536)