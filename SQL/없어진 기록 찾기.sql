/*
- 2026-01-07(2)
- 문제 : 입양 간 기록은 있는데, 보호소에 들어온 기록이 없는 동물의 ID와 이름을 ID순 조회
- 접근법: 1) ANIMAL_OUTS에는 있는데(입양간기록있음), ANIMAL_INS에는 없는(보호소에 들어온 기록없는) 거 추려서 ID출력
*/
SELECT          ANIMAL_ID
                , NAME
FROM            ANIMAL_OUTS
WHERE           ANIMAL_ID NOT IN (
                    SELECT          ANIMAL_ID
                    FROM            ANIMAL_INS
                )
ORDER BY        ANIMAL_ID, NAME


