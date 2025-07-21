import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
# 1. 중복 제거 후 정렬
sorted_unique = sorted(set(arr))
# 2. 각 값을 압축된 좌표로 매핑 (딕셔너리 사용)
coord = {num: idx for idx, num in enumerate(sorted_unique)}
# 3. 원래 입력 순서대로 변환된 좌표 출력
print(' '.join(str(coord[num]) for num in arr))
