/*
- 2025-12-28(1)
- 문제 : 3월에 태어난 여성 회원 목록 출력하기
- 접근법: 시간까지 출력하지 않도록 DATE_FORMAT사용
*/
SELECT          MEMBER_ID
                , MEMBER_NAME
                , GENDER,
                DATE_FORMAT(DATE_OF_BIRTH, "%Y-%m-%d") AS DATE_OF_BIRTH
FROM            MEMBER_PROFILE
WHERE           MONTH(DATE_OF_BIRTH) = '03'
                AND GENDER = 'W'
                AND TLNO IS NOT NULL
ORDER BY        MEMBER_ID