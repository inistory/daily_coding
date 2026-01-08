/*
- 2026-01-08(3)
- 문제 : 만원단위의 가격대 별로 상품 개수를 출력
- 접근법:
        1) 10000원으로 가격을 나누고 FLOOR로 소숫점 떼고, 다시 10000을 곱해서 PRICE_GROUP만들기
        2) 나눠진 그룹별로 COUNT
*/
SELECT          FLOOR(PRICE/10000)*10000 AS PRICE_GROUP
                , COUNT(*) AS PRODUCTS
FROM            PRODUCT
GROUP BY        PRICE_GROUP
ORDER BY        PRICE_GROUP
;
