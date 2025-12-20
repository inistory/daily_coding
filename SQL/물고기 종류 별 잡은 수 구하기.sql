/*
- 문제:물고기의 종류별 물고기의 이름과 잡은 수
FISH_INFO: 잡은 물고기의 정보
FISH_NAME_INFO: 물고기 이름에 대한 정보
- 접근법: 조인해서 FISH_NAME별 COUNT하기
*/
SELECT          COUNT(*) AS FISH_COUNT
                ,FISH_NAME
FROM            FISH_INFO AS FI
INNER JOIN      FISH_NAME_INFO AS FNI
ON              FI.FISH_TYPE = FNI.FISH_TYPE
GROUP BY        FISH_NAME
ORDER BY        FISH_COUNT DESC