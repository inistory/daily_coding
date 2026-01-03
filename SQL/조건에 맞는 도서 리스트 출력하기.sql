/*
- 2026-01-03(2)
- 문제 : 조건에 맞는 도서 리스트 출력하기
- 접근법: DATE_FORMAT로 원하는 형태로 출력
*/
SELECT          BOOK_ID
                , DATE_FORMAT(PUBLISHED_DATE, '%Y-%m-%d') AS PUBLISHED_DATE
FROM            BOOK
WHERE           YEAR(PUBLISHED_DATE) = '2021'
                AND CATEGORY='인문'
ORDER BY        PUBLISHED_DATE