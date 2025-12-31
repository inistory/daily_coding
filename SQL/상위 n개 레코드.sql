/*
- 2025-12-31(2)
- 문제 : 상위 n개 레코드 조회
- 접근법: order by, limit 1 사용
*/
SELECT          NAME
FROM            ANIMAL_INS
ORDER BY        DATETIME
LIMIT           1