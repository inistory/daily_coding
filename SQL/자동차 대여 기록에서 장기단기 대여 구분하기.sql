/*
- 2026-01-08(5)
- 문제 : 대여시작일이 2022-09에 속하는 대여기록에 대해서 대여기간이 30일이상이면 장기 대여, 그렇지않으면 단기대여로 표시하여 출력
- 접근법:
        1) CASE문과 DATEDIFF(END_DATE, START_DATE)를 사용해서 장기대여/단기대여 출력
        2) END_DATE가 앞쪽에 있어야함
*/

SELECT          HISTORY_ID
                , CAR_ID
                , DATE_FORMAT(START_DATE, '%Y-%m-%d') AS START_DATE
                , DATE_FORMAT(END_DATE,'%Y-%m-%d') AS END_DATE
                , CASE
                    WHEN DATEDIFF(END_DATE, START_DATE) +1 >=30 THEN '장기 대여'
                    ELSE '단기 대여'
                END AS RENT_TYPE
FROM            CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE           YEAR(START_DATE) = '2022'
                AND MONTH(START_DATE) = '09'
ORDER BY        HISTORY_ID DESC
;