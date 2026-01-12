/*
- 2026-01-12(1)
- 문제 :
    - (x1, y1), (x2, y2)가 있을 때 x1 = y2 그리고 x2 = y1일 때 symmetric pair라고 함
    - 즉, x와 y의 자리를 바꿨을 때 같으면 됨
    - 페어 중 x < y인 것만 출력
- 접근법:
        1) 같은 테이블을 셀프 조인
        2) x,<y인 경우만 count
        3) 같으면서 페어인건 따로 구해주기
        4) 그 둘을 합쳐주기(UNION)
        5) ORDER BY를 맨아래 써주면 UNION을 한 다음에 그 전체결과물을 정렬해줌
*/
SELECT          X
                , Y
FROM            functions
WHERE           X = Y
GROUP BY        X
                , Y
HAVING COUNT(*) = 2

UNION

SELECT          f1.X
                , f1.Y
FROM            functions AS f1
JOIN            functions AS f2
ON              f1.X = f2.Y
AND             f1.Y = f2.X
WHERE           f1.X < f1.Y
ORDER BY        X
;

