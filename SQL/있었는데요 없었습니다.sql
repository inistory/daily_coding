/*
- 2026-01-07(3)
- 문제 : 보호시작일보다 입양일이 더 빠른 동물의 아이디와 이름, 시작일 빠른 순 조회
- 접근법: 보호시작일(ANIMAL_IDS.DATETIME) > 입양일(ANIMAL_OUTS.DATETIME)이 빠른
*/
SELECT          I.ANIMAL_ID
                , I.NAME
FROM            ANIMAL_INS I
JOIN            ANIMAL_OUTS O
ON              I.ANIMAL_ID = O.ANIMAL_ID
AND             I.DATETIME > O.DATETIME
ORDER BY        I.DATETIME