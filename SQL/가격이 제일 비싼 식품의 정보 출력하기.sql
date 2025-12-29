/*
- 2025-12-29(1)
- 문제 : 제일 비싼 식품 정보 출력
- 접근법: price기준 내림차순 정렬, limit 1로 제일 비싼 거 찾기
*/
SELECT          PRODUCT_ID
                , PRODUCT_NAME
                , PRODUCT_CD, CATEGORY
                , PRICE
FROM            FOOD_PRODUCT
ORDER BY        PRICE DESC
LIMIT           1