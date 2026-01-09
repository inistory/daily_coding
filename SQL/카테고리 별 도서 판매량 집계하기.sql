/*
- 2026-01-09(4)
- 문제 : 도서와 판매량 정보가 있을 때, 2022년1월의 카테고리별 도서 판매량을 합산하고 카테고리, 총 판매량 리스트 출력
- 접근법:
        1) BOOK, BOOK_SALE을 BOOK_ID기준으로 JOIN
        2) 2022년 1월만 WHERE문으로 추리기
        3) 카테고리별 도서 판매량 합산 GROUP BY SUM()으로 구하기
*/
SELECT          B.CATEGORY
                , SUM(S.SALES) AS TOTAL_SALES
FROM            BOOK B
JOIN            BOOK_SALES S
ON              B.BOOK_ID = S.BOOK_ID
WHERE           S.SALES_DATE BETWEEN '2022-01-01' AND '2022-01-31'
GROUP BY        B.CATEGORY
ORDER BY        B.CATEGORY
;