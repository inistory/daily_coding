/*
- 2025-12-29(3)
- 문제 : ADDRESS에 강원도 텍스트 포함된거 필터링
- 접근법: ADDRESS LIKE '강원도%' 써서 찾기
*/
SELECT          FACTORY_ID
                , FACTORY_NAME
                , ADDRESS
FROM            FOOD_FACTORY
WHERE           ADDRESS LIKE '강원도%'
ORDER BY        FACTORY_ID;