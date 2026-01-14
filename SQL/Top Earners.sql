/*
- 2026-01-14(1)
- 문제 :
    - 부서에서 몇명이 가장 많이 벌었는지 (번금액, 몇명)
- 접근법:
    - where절에 서브쿼리 쓰기
    - 원하는 형태 출력을 위해 GROUP BY earning
      (SELECT에서 선언해준 alias는 where절에서는 못써도 groupby에서는 쓸 수 있음)
*/

SELECT          salary * months AS earnings
                , COUNT(*)
FROM            employee
WHERE           salary * months = (
                    SELECT          MAX(salary * months)
                    FROM            employee
                )
GROUP BY        earnings
;