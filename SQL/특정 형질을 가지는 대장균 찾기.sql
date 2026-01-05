/*
- 2026-01-05(3)
- 문제 : 2번 형질이 보유하지 않으면서 1번이나 3번 형질을 보유하고 있는 대장균 개체의 수 출력
- 접근법: n번형질 = 비트마스크상 위치, 1번형질 = 2^0=1, 2번형질=2^1=2, 3번형질=2^2=4
*/
SELECT          COUNT(*) AS COUNT
FROM            ECOLI_DATA
WHERE           (GENOTYPE & 1 OR GENOTYPE & 4)
                AND !(GENOTYPE & 2)