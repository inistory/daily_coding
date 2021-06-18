#https://velog.io/@ju_h2/Python-%EB%B0%B1%EC%A4%80-2212.-%EC%84%BC%EC%84%9C-%ED%92%80%EC%9D%B4-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%83%90%EC%9A%95-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EA%B7%B8%EB%A6%AC%EB%94%94-%EA%B5%AC%ED%98%84-3
n = int(input())
k = int(input())
sensor = list(map(int, input().split()))

## k>n일때 예외처리

if k >= n:
print(0)
else:
sensor.sort()
gap = []
for i in range(1, n):
gap.append((sensor[i]-sensor[i-1], i))
gap.sort()

    standard = [0]
    result = 0
    for i in range(k-1):
        standard.append(gap.pop()[1])
    standard.append(0)

    result = 0
    for i in range(k): # 0, 1
        result += sensor[standard[i+1]-1]-sensor[standard[i]]
    print(result)
