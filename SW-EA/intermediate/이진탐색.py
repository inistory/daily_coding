#이진탐색게임
#두 사람이 c를 이진탐색으로 찾아갈 때, 걸리는 횟수를 비교
#이긴사람출력, 비기면 0출력

def b_search(p,tp):
    start = 1
    end = p
    cnt = 0
    while start<=end:
        tmp =(start + end)//2
        cnt+=1

        if tmp == tp:
            return cnt
        elif tmp < tp:
            start = tmp
        elif tmp > tp:
            end = tmp

T = int(input())
for tc in range(1, T + 1):
    p, pa, pb = map(int,input().split())
    
    if b_search(p,pa) > b_search(p,pb):
        print(f'#{tc} B')
    elif b_search(p,pa) < b_search(p,pb):
        print(f'#{tc} A')
    else:
        print(f'#{tc} 0')
