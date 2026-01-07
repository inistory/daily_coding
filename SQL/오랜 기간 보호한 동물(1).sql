/*
- 2026-01-07(1)
- 문제 : 아직 입양을 못 간 동물 중, 가장 오래 보호소에 있던 동물 3마리의 이름, 보호 시작일 조회
- 접근법: 1) ANIMAL_INS에 있는 동물 중, ANIMAL_OUTS에 없는 동물(입양못간동물) 추리기
         2) 그 중에서 가장 오래 보호소에 있던 동물 3마리 정보(ORDER BY DATETIME LIMIT 3)
*/
SELECT          NAME
                , DATETIME
FROM            ANIMAL_INS
WHERE           ANIMAL_ID NOT IN (
                    SELECT          ANIMAL_ID
                    FROM            ANIMAL_OUTS
                )
ORDER BY        DATETIME
LIMIT           3