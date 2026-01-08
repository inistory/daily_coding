/*
- 2026-01-08(4)
- 문제 : 동물별로 중성화 되었는지 아닌지 파악
- 접근법:
        1) SELECT절에서 CASE WHEN과 LIKE사용해서 분류
*/
SELECT          ANIMAL_ID
                , NAME
                , CASE
                    WHEN SEX_UPON_INTAKE LIKE '%Neutered%'
                         OR SEX_UPON_INTAKE LIKE '%Spayed%' THEN 'O'
                ELSE 'X'
                END AS 중성화
FROM            ANIMAL_INS
ORDER BY        ANIMAL_ID
;
