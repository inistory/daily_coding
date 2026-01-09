/*
- 2026-01-09(5)
- 문제 : 2022년 1월 판매데이터 기준으로 매출액을 구해서 출력
- 접근법:
        1) BOOK, AUTHOR, BOOK_SALES JOIN
        2) 2022년 1월 WHERE로 필터링 (BETWEEN은 양끝을 포함하므로 두 조건쓰기)
        3) 저자 별, 카테고리 별 매출액 산정
*/
SELECT          A.AUTHOR_ID
                , A.AUTHOR_NAME
                , B.CATEGORY
                , SUM(S.SALES*B.PRICE) AS TOTAL_SALES
FROM            BOOK B
JOIN            AUTHOR A
ON              B.AUTHOR_ID = A.AUTHOR_ID
JOIN            BOOK_SALES S
ON              B.BOOK_ID = S.BOOK_ID
WHERE           S.SALES_DATE >= '2022-01-01'
                AND S.SALES_DATE < '2022-02-01'
GROUP BY        A.AUTHOR_ID
                , A.AUTHOR_NAME
                , B.CATEGORY
ORDER BY        B.AUTHOR_ID
                , B.CATEGORY DESC