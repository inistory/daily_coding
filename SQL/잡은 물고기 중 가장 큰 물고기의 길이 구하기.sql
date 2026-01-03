/*
- 2026-01-03(1)
- 문제 : 가장 큰 물고기 구하기
- 접근법: CONCAT(MAX(LENGTH),'cm')로 요구사항에 맞게 출력
*/
SELECT          CONCAT(MAX(LENGTH),'cm') AS MAX_LENGTH
FROM            FISH_INFO
ORDER BY        LENGTH DESC
