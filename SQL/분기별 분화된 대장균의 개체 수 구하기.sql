/*
- 2025-12-26(3)
- 문제 : 분기별 분화된 대장균 개체의 총 수
- 접근법: 
    1)QUARTER로 분기 구분(QUARTER는 1~4를 반환하므로 CONCAT으로 Q를 붙여줌)
    2)SELECT에서 구분한 분기를 기준으로 GROUP BY 진행
*/
SELECT          CONCAT(QUARTER(DIFFERENTIATION_DATE), 'Q') AS QUARTER
                , COUNT(*) AS ECOLI_COUNT
FROM            ECOLI_DATA
GROUP BY        QUARTER
ORDER BY        QUARTER;