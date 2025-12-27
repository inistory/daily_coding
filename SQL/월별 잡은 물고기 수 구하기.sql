/*
- 2025-12-27(1)
- 문제 : 월별 잡은 물고기 수 구하기
- 접근법: MONTH(TIME) 사용
*/
SELECT          COUNT(*) AS FISH_COUNT
                , MONTH(TIME) AS MONTH
FROM            FISH_INFO
GROUP BY        MONTH(TIME)
ORDER BY        MONTH(TIME)