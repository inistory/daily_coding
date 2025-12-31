/*
- 2025-12-31(3)
- 문제 : 아픈 동물 찾기
- 접근법: where조건 사용
*/
SELECT          ANIMAL_ID
                , NAME
FROM            ANIMAL_INS
WHERE           INTAKE_CONDITION = 'sick'
ORDER BY        ANIMAL_ID