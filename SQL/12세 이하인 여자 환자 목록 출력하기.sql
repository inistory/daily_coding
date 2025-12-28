/*
- 2025-12-28(2)
- 문제 : 12세 이하인 여자 환자 목록 출력
- 접근법: 전화 번호 없는 경우 NONE으로 바꾸기 위해 CASE문 사용
*/
SELECT          PT_NAME
                , PT_NO
                , GEND_CD
                , AGE
                , CASE
                    WHEN TLNO IS NULL THEN 'NONE'
                    ELSE TLNO
                END AS TLNO
FROM            PATIENT
WHERE           AGE <=12
                AND GEND_CD='W'
ORDER BY        AGE DESC
                , PT_NAME ASC