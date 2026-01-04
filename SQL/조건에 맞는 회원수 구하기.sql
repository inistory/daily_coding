/*
- 2026-01-04(1)
- 문제 : 2021년 20세이상 29세 이하인 회원수 구하기
- 접근법: where 조건 사용, COUNT(USER_ID)로 유저수 구하기
*/
SELECT          COUNT(USER_ID) AS USERS
FROM            USER_INFO
WHERE           YEAR(JOINED) = '2021'
                AND AGE >= 20
                AND AGE <= 29