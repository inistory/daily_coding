/*
- 2025-12-25
- 문제: 더이상 업그레이드 할 수 없는 아이템 
- 접근법: parent item이 없는 아이템만 추리기 
*/
SELECT          ITEM_ID
                , ITEM_NAME
                , RARITY 
FROM            ITEM_INFO                         
WHERE           ITEM_ID NOT IN (
                SELECT          PARENT_ITEM_ID
                FROM            ITEM_TREE
                WHERE           PARENT_ITEM_ID IS NOT NULL -- NOT IN에서는 NULL이 있으면 안됨
                )
ORDER BY        ITEM_ID DESC;