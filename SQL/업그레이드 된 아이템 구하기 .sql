/*
- 2026-01-06(1)
- 문제 : 업그레이드 된 아이템 구하기: A(부모)-> B -> C(자식, 업그레이트)
- 접근법: 1) 부모 정보를 ITEM_INFO에서 가져오기 완성하기
         2) 완성한 부모 정보를 보고 RARE한 부모의 정보만 남기기
         3) 해당 부모의 자식(T.ITEM_ID)을 기준으로 ITEM_INFO에서 자식의 정보 가져오기
         4) 자식정보 출력, 내림차순 정렬
*/
SELECT          C.ITEM_ID
                , C.ITEM_NAME
                , C.RARITY
FROM            ITEM_TREE T
JOIN            ITEM_INFO I
ON              T.PARENT_ITEM_ID = I.ITEM_ID -- 부모의 ITEM_INFO 가져오기
AND             I.RARITY = 'RARE' -- RARE인 부모구하기
JOIN            ITEM_INFO C
ON              T.ITEM_ID = C.ITEM_ID -- 부모ITEM_ID와의 자식 조인
ORDER BY        C.ITEM_ID DESC;