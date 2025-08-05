def recursion(s, l, r):
    global count #함수안에서 연산을 하기 때문에 이게 전역 변수임을 함수 안에서 선언 필요
    count += 1
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s) - 1)

T = int(input())
for _ in range(T):
    s = input()
    count = 0  # 각 테스트 케이스마다 초기화, 전연 변수 선언
    print(isPalindrome(s), count)