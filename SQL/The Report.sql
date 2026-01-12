/*
- 2026-01-12(3)
- 문제 : name, grade, mark 출력
- 접근법:
    - 8 grade보다 낮은 성적은 제외
    - grade 정렬, 동점자는 name 알파벳 순서 배치
    - 이름이 NULL인 학생들은 grade기준 오름차순 정렬
*/

SELECT          CASE
                    WHEN g.grade >=8 THEN s.name
                END AS name
                , g.grade
                , s.marks
FROM            students AS s
JOIN            grades AS g
ON              s.marks BETWEEN g.min_mark AND g.max_mark -- 학생의 mark가 min_mark, max_mark사이에 있을 때 조인
ORDER BY        g.grade DESC
                , s.name
                , s.marks
;