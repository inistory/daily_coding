#열려있는 창문은 약수 개수가 홀수인 창문만 해당됨(완전제곱수를 세기)
N = int(input())
print(int(N ** 0.5))

#메모리초과
# N = int(input())

# window = [0]*(N+1)

# for i in range(1, N+1):
#     for j in range(1,N+1,i):
#         window[j] = 1 - window[j]
            
# print(sum(window))