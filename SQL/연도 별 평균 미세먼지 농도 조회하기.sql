/*
- 2025-12-26(2)
- 문제: 연도별 1)평균 미세먼지 오염도, 2)평균 초미세먼지 오염도
- 접근법: 수원지역만 필터링, YEAR(YM)로 연도 추출하기, 년도별이니까 YEAR(YM)로 그룹지어서 표기, PM10, PM2.5는 스트링 표기해주기
*/
SELECT          YEAR(YM) AS YEAR
                , ROUND(AVG(PM_VAL1),2) AS 'PM10'
                , ROUND(AVG(PM_VAL2),2) AS 'PM2.5'
FROM            AIR_POLLUTION
WHERE           LOCATION2 = '수원'
GROUP BY        YEAR(YM)
ORDER BY        YEAR(YM) ASC