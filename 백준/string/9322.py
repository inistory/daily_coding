#철벽 보안 알고리즘
test_case =int(input())

for _ in range(test_case):
    n = int(input())
    pub1 = list(map(str,input().split()))
    pub2 = list(map(str,input().split()))
    code = list(map(str,input().split()))
    answer = [False for _ in range(n)]
    rule = {}

    for i, a in enumerate(pub1):
        for j, b in enumerate(pub2):
            if a == b:
                rule[j] = i 

    for i,_ in enumerate(code):
        answer[rule[i]] = code[i]
    
    print(' '.join(answer))