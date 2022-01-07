def solution(triangle):
    for i in range(1, len(triangle)): #첫째줄엔 1개, 둘째줄엔 2개 ...
        for j in range(i + 1): #j는 이전 값보다 하나 많은 갯수
            if j == 0:# 가장 왼쪽 값인 경우
                triangle[i][j] += triangle[i-1][j]
            elif j == i:# 가장 오른쪽 값인 경우
                triangle[i][j] += triangle[i-1][-1]
            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
    return max(triangle[-1]) #마지막 줄의 최댓값