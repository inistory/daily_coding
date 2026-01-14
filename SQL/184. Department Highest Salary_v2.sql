/*
- 2026-01-14(3) [윈도우함수이용풀이]
- 문제 : 부서별로 highest salary를 가진 employee를 개별출력
        , 부서별 출력이아니라, employee별 출력임, 부서별로 출력하면 여러 employee를 출력할 수 없음
- 접근법:
    - RANK()활용해서 부서별로 많이버는 순으로 순위를 매김
    - 전체에서 RANK를 매기는게 아니라 각 부서별로 RANK를 매겨줘야하기 떄문에 PARTITION BY departmentId 사용
    - salary를 기준으로 내림차순 정렬을 해줘야하기 때문에 ORDER BY salary DESC 사용
    - 윈도우함수를 사용해서 연산한 결과를 바로 WHERE절에서 필터링을 할 수 없어서 서브쿼리로 감싸주기
*/
SELECT          d.name AS Department
                , e.name AS Employee
                , e.salary AS Salary

FROM(
    SELECT          departmentId
                    , name
                    , salary
                    , RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS rk
    FROM            employee
    ) AS e
INNER JOIN      department AS d
ON              e.departmentId = d.id
WHERE           rk = 1
;
