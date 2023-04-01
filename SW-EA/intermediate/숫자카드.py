#test10에서 fail ->  카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력 조건 추가
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
    max_value = tmp[key]
    for key, value in sorted(tmp.items(),reverse=True):#오름차순 정렬
        if max_value == value:
            print(f"#{test_case} {key} {value}")
            break