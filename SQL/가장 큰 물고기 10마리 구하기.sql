/*
- 2025-12-29(2)
- 문제 : 가장 큰 물고기 10마리
- 접근법: limit10
*/
SELECT          ID
                , LENGTH
FROM            FISH_INFO
ORDER BY        LENGTH DESC, ID
LIMIT           10

