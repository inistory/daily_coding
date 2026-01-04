/*
- 2026-01-04(3)
- 문제 : 중복제거
- 접근법: COUNT(DISTINCT NAME)을 통해 중복 제거
*/
SELECT          COUNT(DISTINCT NAME) AS count
FROM            ANIMAL_INS
WHERE           NAME IS NOT NULL