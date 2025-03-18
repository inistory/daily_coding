#문자열 교환

s = input().strip()

# 1. 문자열에서 'a'의 개수를 센다.
count_a = s.count('a')

# 2. 문자열을 두 번 이어붙여 원형으로 처리
s_extended = s + s

# 3. 슬라이딩 윈도우를 사용하여 최소 교환 횟수 계산
min_swaps = float('inf')
current_b_count = 0

# 초기 윈도우에서 'b'의 개수를 센다.
for i in range(count_a):
    if s_extended[i] == 'b':
        current_b_count += 1

min_swaps = current_b_count

# 슬라이딩 윈도우를 이동하며 최소값 갱신
for i in range(1, len(s)):
    # 윈도우의 왼쪽 끝 문자 제거
    if s_extended[i - 1] == 'b':
        current_b_count -= 1
    # 윈도우의 오른쪽 끝 문자 추가
    if s_extended[i + count_a - 1] == 'b':
        current_b_count += 1
    # 최소값 갱신
    min_swaps = min(min_swaps, current_b_count)

print(min_swaps)