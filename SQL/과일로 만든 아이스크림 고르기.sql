/*
- 2025-12-30(1)
- 문제 : 과일로 만든 아이스크림
- 접근법: join 후 fruit_based 필터링
*/
SELECT          F.FLAVOR
FROM            FIRST_HALF AS F
JOIN            ICECREAM_INFO I
ON              F.FLAVOR = I.FLAVOR
WHERE           F.TOTAL_ORDER > 3000
                AND I.INGREDIENT_TYPE = 'fruit_based'
ORDER BY        F.TOTAL_ORDER DESC