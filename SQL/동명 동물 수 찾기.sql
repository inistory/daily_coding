/*
- 2026-01-08(1)
- 문제 : 동물 보호소에 들어온 동물 이름 중 두 번 이상 쓰인 이름과 해당 이름이 쓰인 횟수를 조회
- 접근법:
        1) 들어온 돌울 이름 기준으로 GROUP BY해서 몇번등장했는지 COUNT하고
        2) Having으로 두번이상 등장한 동물 이름을 필터링
*/
SELECT          NAME
                , COUNT(*) AS COUNT
FROM            ANIMAL_INS
WHERE           NAME IS NOT NULL
GROUP BY        NAME
HAVING          COUNT(*) >=2
ORDER BY        NAME