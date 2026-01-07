/*
- 2026-01-07(5)
- 문제 : 상품코드 별 매출액(판매가*판매량) 합계 출력 / 매출액 desc, 상품코드 asc
- 접근법:
        1) PRODUCT, OFFLINE_SALE을 PRODUCT_ID기준 INNER JOIN
        2) GROUP BY P.PRODUCT_CODE
        3) 판매가*판매량: P.PRICE*O.SALES_AMOUNT

*/
SELECT          P.PRODUCT_CODE
                , P.PRICE * SUM(O.SALES_AMOUNT) AS SALES
FROM            PRODUCT P
JOIN            OFFLINE_SALE O
ON              P.PRODUCT_ID = O.PRODUCT_ID
GROUP BY        P.PRODUCT_CODE
ORDER BY        SALES DESC
                , P.PRODUCT_CODE

