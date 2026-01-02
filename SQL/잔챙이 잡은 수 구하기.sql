/*
- 2026-01-02(2)
- 문제 : 잔챙이 잡은 수 구하기
- 접근법: LENGTH IS NULL이 잔챙이들임
*/
SELECT          COUNT(ID) AS FISH_COUNT
FROM            FISH_INFO
WHERE           LENGTH IS NULL