def solution(bandage, max_health, attacks):
    t, x, y = bandage  # 시전 시간, 초당 회복량, 추가 회복량
    current_health = max_health
    skill_time_count = 0  # 연속 성공 시간
    cur_time = 0  # 현재 시간
    attack_idx = 0  # 공격 인덱스

    while cur_time <= 1000:  # 문제에서 시간 범위가 최대 1000으로 주어짐
        # 공격 확인
        if attack_idx < len(attacks) and cur_time == attacks[attack_idx][0]:
            # 공격 발생
            damage = attacks[attack_idx][1]
            current_health -= damage
            skill_time_count = 0  # 연속 성공 초기화
            attack_idx += 1  # 다음 공격으로 이동
        else:
            # 공격이 없는 경우 체력 회복
            if current_health > 0:
                skill_time_count += 1
                current_health += x  # 초당 회복량
                # 체력이 최대치를 넘지 않도록 제한
                if current_health > max_health:
                    current_health = max_health

                # t초 연속 성공 시 추가 회복
                if skill_time_count == t:
                    current_health += y
                    if current_health > max_health:
                        current_health = max_health
                    skill_time_count = 0

        # 캐릭터 사망 체크
        if current_health <= 0:
            return -1

        # 시간 증가
        cur_time += 1

        # 공격이 모두 끝났고 체력이 감소하지 않으면 종료
        if attack_idx >= len(attacks) and skill_time_count == 0:
            break

    return current_health
