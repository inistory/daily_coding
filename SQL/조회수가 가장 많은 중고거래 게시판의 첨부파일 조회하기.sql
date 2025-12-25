/*
- 2025-12-25(3)
- 문제: 조회수가 가장 많은 중고고래 게시판의 첨부파일 조회
- 풀이법: 조회수가 가장 많은걸 조회하기 위해 조회 수 기준 내림차순 정렬, 그리고 LIMIT 1 적용, CONCAT 사용
*/
WITH MAX_BOARD_ID AS (
            SELECT          BOARD_ID
            FROM            USED_GOODS_BOARD
            ORDER BY        VIEWS DESC
            LIMIT           1
)
SELECT          CONCAT('/home/grep/src/', BOARD_ID,'/', FILE_ID, FILE_NAME, FILE_EXT) AS FILE_PATH
FROM            USED_GOODS_FILE
WHERE           BOARD_ID IN (
                    SELECT BOARD_ID 
                    FROM MAX_BOARD_ID
                )
ORDER BY        FILE_ID DESC;