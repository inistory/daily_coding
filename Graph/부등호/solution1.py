# n = int(input()) #부등호 개수
# #부등호
# sign = input().split()
# #숫자 개수 = 부등호개수+1
# max_list = list([i for i in range(0,n+1)])
# min_list = list([i for i in range(9,9-(n+1),-1)])

# print(max_list)
# print(min_list)
# print(sign)

#https://rebas.kr/755
n = int(input())
sign = input().split()
c = [False]*10
mx, mn = "", ""

def possible(i, j, k):
    if k == '<':
        return i < j
    if k == '>':
        return i > j
    return True

def solve(cnt, s):
    global mx, mn
    if cnt == n+1:
        if not len(mn):
            mn = s
        else:
            mx = s
        return
    for i in range(10):
        if not c[i]:
            if cnt == 0 or possible(s[-1], str(i), sign[cnt-1]):
                c[i] = True
                solve(cnt+1, s+str(i))
                c[i] = False

solve(0, "")
print("%s\n%s" % (mx, mn))


출처:  [PROJECT REBAS]
