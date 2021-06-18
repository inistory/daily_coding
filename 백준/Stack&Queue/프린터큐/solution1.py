#https://assaeunji.github.io/python/2020-05-04-bj1966/

test_cases = int(input()) #몇번 테스트할건지

for _ in range(test_cases):
    n,m = list(map(int, input().split( ))) #n:문서의수 #m:궁금한문서의 큐에서의 위치
    imp = list(map(int, input().split( ))) #궁금한 문서의 중요도
    idx = list(range(len(imp))) #문서 마다 고유 인덱스를 생성
    idx[m] = 'target' #m번째 인덱스를 target으로 둔다.

    # 순서
    order = 0
    
    while True: #imp의 첫번째 값이 최대값이 될 때까지 가장 첫 번째 값을 맨 뒤로 보내는 FIFO를 반복
        # 첫번째 if: imp의 첫번째 값 = 최댓값?
        if imp[0]==max(imp): #첫번째 값이 최대값이 되면 order를 하나 증가시키는 것이다.
            order += 1
                        
            # 두번째 if: idx의 첫 번째 값 = "target"?
            if idx[0]=='target': #idx의 첫 번째 값이 target이라면
                print(order) #order를 출력하고 반복을 중단
                break
            else:#그렇지 않다면 imp와 idx의 첫 번째 값을 제거
                imp.pop(0) #imp의 순서가 바뀔 때마다 같이 순서를 바꿔줘야만 한다
                idx.pop(0)

        else:
            imp.append(imp.pop(0))
            idx.append(idx.pop(0))        