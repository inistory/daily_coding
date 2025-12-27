/*
- 2025-12-27(3)
- 문제 : HR_EMPLOYEES(회사사원정보), HR_GRADE(사원평가정보)기반 평가 등급과 성과금 조회하기
- 접근법: HR_GRADE를 보면 한사람당 점수가 두개씩 있다. GROUP BY로 EMP_NO별로 묶은 후 SCORE의 평균을 기준으로 GRADE와 BONUS를 계산, AVG(SCORE)계산이 SELECT문에서 반복되지않도록 JOIN에서 미리 구해놓기
*/
SELECT          E.EMP_NO
                , E.EMP_NAME
                , CASE
                        WHEN G.AVG_SCORE >= 96 THEN 'S'
                        WHEN G.AVG_SCORE >= 90 THEN 'A'
                        WHEN G.AVG_SCORE >= 80 THEN 'B'
                        ELSE 'C'
                END AS GRADE
                , CASE
                        WHEN G.AVG_SCORE >= 96 THEN E.SAL * 0.2
                        WHEN G.AVG_SCORE >= 90 THEN E.SAL * 0.15
                        WHEN G.AVG_SCORE >= 80 THEN E.SAL * 0.10
                        ELSE 0
                END AS BONUS
FROM            HR_EMPLOYEES AS E
JOIN            (
                SELECT          EMP_NO
                                , AVG(SCORE) AS AVG_SCORE
                FROM            HR_GRADE
                GROUP BY        EMP_NO
    
                ) AS G
ON              E.EMP_NO = G.EMP_NO
ORDER BY        E.EMP_NO;