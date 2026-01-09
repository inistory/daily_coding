/*
- 2026-01-09(1)
- 문제 : 입양 시각 구하기(2)
- 접근법:
        1) 변수로 0~23 시각 테이블 생성
        2) ANIMAL_OUTS를 시간(HOUR)별로 집계
        3) LEFT JOIN 후 NULL은 0으로 치환
*/
SET @HOUR := -1; -- 변수 초기화(0부터 나오게 하려고)

SELECT          H.HOUR
                , IFNULL(C.CNT, 0) AS COUNT --NULL값이 있다면 0으로 치환
FROM            (
                SELECT          (@HOUR := @HOUR + 1) AS HOUR -- 0부터 1씩 HOUR를 증가
                FROM            ANIMAL_OUTS
                WHERE           @HOUR < 23
                ) H -- 0~23 시간표 만들기
LEFT JOIN       (
                SELECT          HOUR(DATETIME) AS HOUR
                                , COUNT(*) AS CNT
                FROM            ANIMAL_OUTS
                GROUP BY        HOUR(DATETIME)
                ) C -- 시간대별 입양 건수 세기
ON              H.HOUR = C.HOUR -- 시간대 기준으로 조인, 0~23이 포함되도록 LEFT조인
ORDER BY        H.HOUR
;
