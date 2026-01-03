/*
- 2026-01-03(3)
- 문제 : 아이템 총합 구하기
- 접근법: SUM으로 아이템 총합구하기
*/
SELECT          SUM(PRICE) AS TOTAL_PRICE
FROM            ITEM_INFO
WHERE           RARITY = 'LEGEND'