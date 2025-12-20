/*
- 문제:물고기의 종류별 물고기의 이름과 잡은 수
- 접근법: 조인해서 FISH_NAME별 COUNT하기
*/
SELECT          COUNT(*) AS FISH_COUNT
                ,FISH_NAME
FROM            FISH_INFO AS FI /*잡은 물고기*/
INNER JOIN      FISH_NAME_INFO AS FNI /*물고기 이름*/
ON              FI.FISH_TYPE = FNI.FISH_TYPE
GROUP BY        FISH_NAME
ORDER BY        FISH_COUNT DESC