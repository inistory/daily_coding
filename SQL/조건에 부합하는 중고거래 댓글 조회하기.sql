/*
- 2026-01-04(2)
- 문제 : 조건에 부합하는 중고거래 댓글 조회
- 접근법: BOARD_ID로 조인하고 각 필드에서 필요한 값 가져오기. DATE_FORMAT써서 시간 안나오게하기
*/
SELECT          B.TITLE
                , B.BOARD_ID
                , R.REPLY_ID
                , R.WRITER_ID
                , R.CONTENTS
                , DATE_FORMAT(R.CREATED_DATE, '%Y-%m-%d') AS CREATED_DATE
FROM            USED_GOODS_BOARD B
JOIN            USED_GOODS_REPLY R
ON              B.BOARD_ID = R.BOARD_ID
WHERE           YEAR(B.CREATED_DATE) = '2022'
                AND MONTH(B.CREATED_DATE) = '10'
ORDER BY        R.CREATED_DATE
                , B.TITLE