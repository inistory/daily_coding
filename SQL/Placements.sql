/*
- 2026-01-13(2)
- 문제 : 본인보다 베스트 프렌드의 salary가 높은 사람 출력 (friend기준으로)
- 접근법:
    - friend를 기준으로 패키지 테이블을 두 번 붙이기
    - 1)본인의 salary붙이기, 2)friend의 salary를 붙이기
    - 그 다음, WHERE절에서 친구의 salary가 더 높으면 출력하도록 함
    - 이름 출력을 위해 한 번 더 조인
 */

SELECT          s.name
FROM            friends AS f
INNER JOIN      packages AS ms
ON              f.id = ms.id
INNER JOIN      packages AS fs
ON              f.friend_id = fs.id
INNER JOIN      students AS s
ON              s.id = f.id
WHERE           ms.salary < fs.salary
ORDER BY        fs.salary
;


