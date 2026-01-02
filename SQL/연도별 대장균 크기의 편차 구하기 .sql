/*
- 2026-01-02(3)
- 문제 : 연도별 대장균 크기의 편차 구하기
- 접근법: PARTITION BY 윈도우 함수 사용(group by보다 원래 행수를 그대로 유지해서 좋음)
        1) 현재행 선택
        2) 현재 행의 YEAR을 가진 행들만 모아서 파티션 형성
        3) 그 파티션에서 MAX(SIZE_OF_COLONY) 계산
        4) 그 결과에서 SIZE_OF_COLONY를 뺌
*/
/*더 좋은 풀이*/
SELECT          YEAR(DIFFERENTIATION_DATE) AS YEAR
                , MAX(SIZE_OF_COLONY) OVER (
                    PARTITION BY YEAR(DIFFERENTIATION_DATE)
                  ) - SIZE_OF_COLONY AS YEAR_DEV
                , ID
FROM            ECOLI_DATA
ORDER BY        YEAR
                , YEAR_DEV;



/*내가 푼 풀이*/
SELECT          YEAR(DIFFERENTIATION_DATE) AS YEAR
                , (
                    SELECT          MAX(SIZE_OF_COLONY)
                    FROM            ECOLI_DATA
                    WHERE           YEAR(DIFFERENTIATION_DATE) = YEAR
                ) - SIZE_OF_COLONY AS YEAR_DEV
                , ID
FROM            ECOLI_DATA
ORDER BY        YEAR
                , YEAR_DEV;