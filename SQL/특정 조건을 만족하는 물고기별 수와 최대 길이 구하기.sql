/*
- 2025-12-27(2)
- 문제 : 특정 조건을 만족하는 물고기별 수와 최대 길이 구하기
- 접근법: GROUP BY 집계 후 필터링이므로 where대신 having 사용, '평균'길이가 33이상인 물고기들을 필터링하는거니까 AVG를 사용
*/
SELECT          COUNT(*) AS FISH_COUNT
                , MAX(IFNULL(LENGTH,10)) AS MAX_LENGTH
                , FISH_TYPE
FROM            FISH_INFO
GROUP BY        FISH_TYPE
HAVING          AVG(IFNULL(LENGTH,10)) >= 33
ORDER BY        FISH_TYPE