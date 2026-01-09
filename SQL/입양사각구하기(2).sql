/*
- 2026-01-09
- 문제 : 입양 시각 구하기(2)
- 접근법:
        1) 변수로 0~23 시각 테이블 생성
        2) ANIMAL_OUTS를 시간(HOUR)별로 집계
        3) LEFT JOIN 후 NULL은 0으로 치환
*/
SET @HOUR := -1;

SELECT          H.HOUR
                , IFNULL(C.CNT, 0) AS COUNT
FROM            (
                SELECT (@HOUR := @HOUR + 1) AS HOUR
                FROM ANIMAL_OUTS
                WHERE @HOUR < 23
                ) H
LEFT JOIN       (
                SELECT HOUR(DATETIME) AS HOUR
                        , COUNT(*) AS CNT
                FROM ANIMAL_OUTS
                GROUP BY HOUR(DATETIME)
                ) C
ON              H.HOUR = C.HOUR
ORDER BY        H.HOUR
;
