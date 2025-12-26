/*
- 문제: 2021년도 물고기 필터링
- 접근법: YEAR로 TIME감싸면 년도 구할 수 있음 
*/
SELECT          COUNT(*) AS FISH_COUNT
FROM            FISH_INFO
WHERE           YEAR(TIME) = 2021;