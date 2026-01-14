/*
- 2026-01-14(2)
- 문제 : 부서별로 highest salary를 가진 employee 출력
- 접근법:
    - WITH문으로 부서별로 얼마를 받아야 가장 많이 받은건지 확인
    - 부서별 최대치에 해당하는 부서, 직원, 급여 출력
*/

WITH
dhs AS ( -- 부서별로 얼마를 받아야 가장 많이 받는건지
    SELECT          departmentId
                    , MAX(salary) AS dhs
    FROM            employee
    GROUP BY        departmentId
)

SELECT          d.name AS Department
                , e.name AS Employee
                , e.salary AS Salary
FROM            dhs
INNER JOIN      employee AS e
ON              dhs.departmentId = e.departmentId
AND             dhs.dhs = e.salary
INNER JOIN      department AS d
ON              e.departmentId = d.Id
;