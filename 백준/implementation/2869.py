A, B, V = map(int, input().split())

# 하루 동안 올라가는 순수 높이
net_height_per_day = A - B

# 목표 높이에서 첫날 올라간 높이를 뺀 후, 하루 동안 올라가는 순수 높이로 나눕니다.
days = (V - B - 1) // net_height_per_day + 1

print(days)