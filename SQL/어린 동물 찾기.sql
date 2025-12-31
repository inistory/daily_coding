/*
- 2026-01-01(1)
- 문제 : 어린 동물 찾기
- 접근법: INTAKE_CONDITION !='Aged' 로 필터링
*/
SELECT          ANIMAL_ID
                , NAME
FROM            ANIMAL_INS
WHERE           INTAKE_CONDITION !='Aged'
ORDER BY        ANIMAL_ID