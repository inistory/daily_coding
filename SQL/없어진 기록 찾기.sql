/*
- 2026-01-07(2)
- 문제 : 입양 간 기록은 있는데, 보호소에 들어온 기록이 없는 동물의 ID와 이름을 ID순 조회
- 접근법: 1) ANIMAL_OUTS에는 있는데(입양간기록있음), ANIMAL_INS에는 없는(보호소에 들어온 기록없는) 거 추려서 ID출력
        (ANIMAL_OUTS기준으로 LEFT JOIN하면 ANIMAL_OUTS에 없는건 NULL이 됨을 활용)
*/
SELECT          O.ANIMAL_ID
                , O.NAME
FROM            ANIMAL_OUTS O
LEFT JOIN       ANIMAL_INS I
ON              O.ANIMAL_ID = I.ANIMAL_ID
WHERE           I.ANIMAL_ID IS NULL
ORDER BY        O.ANIMAL_ID
                , O.NAME