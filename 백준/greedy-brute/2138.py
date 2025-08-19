import sys
input = sys.stdin.readline

def toggle(arr, i):
    for j in [i - 1, i, i + 1]:
        if 0 <= j < len(arr):
            arr[j] = 1 - arr[j]

#i-1번째 전구가 target[i-1]와 같으면 스위치누르기
#
def simulate(curr, target):
    n = len(curr)
    temp = curr[:]
    count = 0

    for i in range(1, n):
        if temp[i - 1] != target[i - 1]:
            toggle(temp, i)
            count += 1

    return count if temp == target else float('inf')

N = int(input())
curr = list(map(int, input().strip()))
target = list(map(int, input().strip()))

#어떤 전구를 바꿀지 결정하는 기준은 바로 앞 전구의 값에 따라 정해짐
#i-1번째 전구가 target[-1]과 다르면, i번째 스위치를 눌러서 i-1을 바꿔야함

# 시도 1: 첫 번째 스위치 누르지 않음
res1 = simulate(curr, target)

# 시도 2: 첫 번째 스위치 누름
curr2 = curr[:]#curr복사본만들기
toggle(curr2, 0)
res2 = simulate(curr2, target) + 1

answer = min(res1, res2)
print(answer if answer != float('inf') else -1)
