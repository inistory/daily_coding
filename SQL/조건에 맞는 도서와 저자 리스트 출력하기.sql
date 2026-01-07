/*
- 2026-01-07(4)
- 문제 : 경제 카테고리에 속하는 도서들의 ID, 저자명, 출판일 / 출판일 기준 오름차순
- 접근법: 1) BOOK, AUTHOR 테이블을 AUTHOR_ID기준으로 INNER JOIN
         2) 조인할 때 AND B.CATEGORY = '경제'로 조인 대상을 제한
*/
SELECT          BOOK_ID
                , A.AUTHOR_NAME
                , DATE_FORMAT(B.PUBLISHED_DATE, "%Y-%m-%d") AS PUBLISHED_DATE
FROM            BOOK B
JOIN            AUTHOR A
ON              B.AUTHOR_ID = A.AUTHOR_ID
AND             B.CATEGORY = '경제'
ORDER BY        B.PUBLISHED_DATE