/*
- 2025-12-24(1)
- 문제: ROOT 아이템(parent가 없는 아이템) 구하기
- 접근법: ROOT_ITEM_ID를 만들어서 left join으로 root item만 filtering
*/
WITH            ROOT_ITEM_ID AS (
                SELECT          ITEM_ID
                FROM            ITEM_TREE
                WHERE           PARENT_ITEM_ID is null
)
SELECT          R.ITEM_ID
                , I.ITEM_NAME
FROM            ROOT_ITEM_ID R
LEFT JOIN       ITEM_INFO I
ON              R.ITEM_ID = I.ITEM_ID