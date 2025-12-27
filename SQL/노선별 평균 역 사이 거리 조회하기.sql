/*
- 2025-12-23(1)
- 문제: 노선별 평균 역 사이 거리 조회
- 접근법:CONCAT으로 km 붙이기, ROUND로 소숫점 표시하기
*/
SELECT          ROUTE
                , CONCAT(ROUND(SUM(D_BETWEEN_DIST),1), 'km') AS TOTAL_DISTANCE
                , CONCAT(ROUND(AVG(D_BETWEEN_DIST),2), 'km') AS AVERAGE_DISTANCE
FROM            SUBWAY_DISTANCE
GROUP BY        ROUTE
ORDER BY        SUM(D_BETWEEN_DIST) DESC