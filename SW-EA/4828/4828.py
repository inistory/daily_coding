T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    #N개의 양수
    N = int(input())
    test = list(map(int,input().split()))
    test.sort()
    # print(N,test)
    print(f'#{test_case} {test[-1]-test[0]}')