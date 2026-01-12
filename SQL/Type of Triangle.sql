/*
- 2026-01-12(2)
- 문제 : 이등변 삼각형(Isosceles), 정삼각형(Equilateral), 세변이모두다른삼각형(Scalene), 삼각형이아닌거 구분해서 출력하기
- 접근법:
    - 세번이 같다 -> 정삼각형
    - 두변의 길의 합이 나머지 하나의 길이보다 작으면 삼각형이 성립을 안함
    - 두 변이 같으면 이등변 삼각형
*/
SELECT          CASE
                    WHEN A + B <= C OR A + C <= B OR B + C <= A THEN 'Not A Triangle'
                    WHEN A = B AND B = C THEN 'Equilateral'
                    WHEN A = B OR B = C OR A = C THEN 'Isosceles'
                    WHEN A != B AND B != C AND A != C THEN 'Scalene'
                END
FROM            triangles
;

