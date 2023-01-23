#test10에서 fail
T = int(input())
for test_case in range(1, T + 1):
    tmp = {}
    N = int(input())#카드 장수
    lst = list(input())
    for _,n in enumerate(lst):
        if n not in tmp:
            tmp[n] = 1
        else: 
            tmp[n] +=1

    key = max(tmp,key=tmp.get)
    value = tmp[key]
    print(f"#{test_case} {key} {value}")
