/*
- 2026-01-06(2)
- 문제 : 평균 일일 대여 요금 구하기
- 접근법: ROUND(AVG(DAILY_FEE) 사용
*/
SELECT          ROUND(AVG(DAILY_FEE),0) AS AVERAGE_FEE
FROM            CAR_RENTAL_COMPANY_CAR
WHERE           CAR_TYPE = 'SUV'