def solution(answers): 
    answer = [] 
    student1 = [1, 2, 3, 4, 5] 
    student2 = [2, 1, 2, 3, 2, 4, 2, 5] 
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] 
    j=0 
    a=0 
    for i in range(len(answers)): 
        if student1[j] == answers[i]: 
            a+=1 
            j+=1 
        else: 
            j+=1 
        if j ==len(student1): 
            j=0 
    j=0 
    b=0 
    for i in range(len(answers)): 
        if student2[j] == answers[i]: 
            b+=1 
            j+=1 
        else: 
            j+=1 
        if j ==len(student2): 
            j=0 
    j=0 
    c=0         
    for i in range(len(answers)): 
        if student3[j] == answers[i]: 
            c+=1 
            j+=1 
        else: 
            j+=1 
        if j ==len(student3): 
            j=0 
   #맞은 갯수 비교- 1) 가장 큰 수 구하기  
    max = a 
    if a        max =b 
    if max < c: 
        max = c 
    #맞은 갯수 비교- 2) 큰수와 각 학생의 맞친갯수 비교 
    if max == a: 
        answer.append(1) 
    if max == b: 
        answer.append(2) 
    if max == c: 
        answer.append(3) 
         
    return answer