/*
- 2026-01-10(3)
- 문제 : 매니저보다 많이 번 employees 찾기
- 접근법:
        1) E.managerId = M.id로 조인
        2) E.salary > M.salary로 매니저보다 많이 번 employees찾기
*/
SELECT          E.name AS Employee
FROM            Employee E
LEFT JOIN            Employee M
ON              E.managerId = M.id
WHERE           E.salary > M.salary
