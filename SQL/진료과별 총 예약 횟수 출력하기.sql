/*
- 2026-01-08(2)
- 문제 : 동물 보호소에 들어온 동물 이름 중 두 번 이상 쓰인 이름과 해당 이름이 쓰인 횟수를 조회
- 접근법:
        1) GROUP BY로 진료과코드 별로 조회
        2) WHERE에서 APNT_YMD LIKE '2022-05%'로 2022-05를 필터링
*/
SELECT          MCDP_CD AS '진료과 코드'
                , COUNT(*) AS '5월예약건수'
FROM            APPOINTMENT
WHERE           APNT_YMD LIKE '2022-05%'
GROUP BY        MCDP_CD
ORDER BY        COUNT(*)
                , MCDP_CD
