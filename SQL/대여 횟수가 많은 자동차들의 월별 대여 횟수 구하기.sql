/*
- 2026-01-09(3)
- 문제 : 대여횟수가 5회 이상인 자동차들에 대해 해당 기간 동안의 월별 자동차 ID별 총 대여횟수 출력
- 접근법:
        1) 2022년 8월부터 2022년 10월기간 추리기(WHERE  START_DATE BETWEEN '2022-08-01' AND '2022-10-31')
        2) 대여횟수 5회 이상인 자동차 추리기(서브쿼리)
        3) 대여횟수를 ID별로 출력
        4) 월별, 자동차아이디별 대여횟수 COUNT
        5) 대여횟수 0인 경우는 COUNT가 세지 않기 때문에 자동 제외
*/
SELECT          MONTH(START_DATE) AS MONTH
                , CAR_ID
                , COUNT(*) AS RECORDS -- 대여횟수
FROM            CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE           START_DATE BETWEEN '2022-08-01' AND '2022-10-31'
AND             CAR_ID IN (
                SELECT          CAR_ID
                FROM            CAR_RENTAL_COMPANY_RENTAL_HISTORY
                WHERE           START_DATE BETWEEN '2022-08-01' AND '2022-10-31'
                GROUP BY        CAR_ID
                HAVING          COUNT(*) >= 5
                )
GROUP BY        MONTH
                , CAR_ID -- 월별, 자동차 아이디별
ORDER BY        MONTH
                , CAR_ID DESC
