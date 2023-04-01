#가장큰수,가장작은수, 2번째가장큰수, 2번째가장작은수...
#인덱싱을 활용하면 되지않을까

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    lst = list(map(int, input().split()))

    lst.sort()
    result = []
    for i in range(int(n/2)):
        if n%2==0: 
            result.append(lst[n-1-i])
            result.append(lst[i])
        else:
            if n/2 == i:
                result.append(lst[i])
            else:
                result.append(lst[n+1-i],lst[i])

    print(f'#{test_case}',*result[:10])


