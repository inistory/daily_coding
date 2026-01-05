/*
- 2026-01-05(1)
- 문제 : 최댓값 구하기
- 접근법: 내림차순 정렬 후 제일 위에꺼 출력
*/
SELECT          DATETIME
FROM            ANIMAL_INS
ORDER BY        DATETIME DESC
LIMIT           1