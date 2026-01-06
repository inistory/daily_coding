/*
- 2026-01-06(3)
- 문제 : 특정 물고기를 잡은 총 수 구하기
- 접근법: 특정 물고기를 추리고 해당 물고기의 정보를 가져와서 count
*/
WITH BS AS (
    SELECT          FISH_TYPE
    FROM            FISH_NAME_INFO
    WHERE           FISH_NAME IN ('BASS','SNAPPER')
)

SELECT          COUNT(*) AS FISH_COUNT
FROM            FISH_INFO F
JOIN            BS
ON              BS.FISH_TYPE = F.FISH_TYPE;