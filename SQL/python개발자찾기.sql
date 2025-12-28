/*
- 2025-12-28(3)
- 문제 : python개발자 찾기
- 접근법: 스킬1,2,3에 python이 있는 개발자 조회
*/
SELECT          ID
                , EMAIL
                , FIRST_NAME
                , LAST_NAME
FROM            DEVELOPER_INFOS
WHERE           'Python' IN (SKILL_1, SKILL_2, SKILL_3)
ORDER BY        ID