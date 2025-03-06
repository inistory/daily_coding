import sys
S = sys.stdin.readline().strip()
n = 0
while len(S):
    n += 1 # 1칸씩 찾기
    num = str(n)
    while len(num) and len(S): #둘 다 아직 숫자가 있고
        if num[0] == S[0]: #만약 n의 앞자리가 S의 앞자리랑 같으면
            S = S[1:] # 앞자리 잘라내
        num = num[1:] # 앞자리 이동
print(n)


#이렇게하면 시간초과가 납니당ㅠㅠ
#문자열 이어붙이기(generated += str(n))가 비효율적
# import sys
# def find_minimum_N(s):
#     n = 1
#     generated = ""
    
#     while True:
#         generated += str(n)  # N을 1부터 차례대로 이어붙임
#         if s in generated:   # 주어진 문자열이 포함되면 종료
#             return n
#         n += 1

# s = sys.stdin.read().strip()
# print(find_minimum_N(s))
