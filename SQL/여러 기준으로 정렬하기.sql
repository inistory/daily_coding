/*
- 2026-01-01(2)
- 문제 : 여러기준으로 정렬하기
- 접근법: DATETIME DESC로 역순 정렬
*/
SELECT          ANIMAL_ID
                , NAME
                , DATETIME
FROM            ANIMAL_INS
ORDER BY        NAME
                , DATETIME DESC