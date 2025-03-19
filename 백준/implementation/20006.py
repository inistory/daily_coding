
p, m = map(int,(input().split()))
players = []

# 플레이어 정보 입력
for _ in range(p):
    l, n = input().split()
    players.append((int(l), n))
    
rooms = []  # 방 리스트

for level, nickname in players:
    placed = False
    for room in rooms:
        # 방에 입장 가능한지 확인
        if room['min_level'] <= level <= room['max_level'] and len(room['players']) < m:
            room['players'].append((level, nickname))
            placed = True
            break

    # 입장 가능한 방이 없으면 새로운 방 생성
    if not placed:
        rooms.append({
            'min_level': level - 10,
            'max_level': level + 10,
            'players': [(level, nickname)]
        })

# 결과 출력
for room in rooms:
    if len(room['players']) == m:
        print("Started!")
    else:
        print("Waiting!")
    # 닉네임 사전순 정렬 후 출력
    for player in sorted(room['players'], key=lambda x: x[1]):
        print(player[0], player[1])