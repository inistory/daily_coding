/*
- 2026-01-02(1)
- 문제 : 인기있는 아이스크림
- 접근법: desc, asc 정렬
*/
SELECT          FLAVOR
FROM            FIRST_HALF
ORDER BY        TOTAL_ORDER DESC
                , SHIPMENT_ID