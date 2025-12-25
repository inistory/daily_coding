/*
- 2025-12-24(2)
- 문제: 잡은 물고기의 평균 길이 구하기
- 접근법: IFNULL를 써서 LENGTH값이 NULL이면 10을 쓸 수 있도록함, AVG로 평균값 구하고, 소수 점 둘째자리까지 반올림
*/
SELECT          ROUND(AVG(IFNULL(LENGTH, 10)),2) AS AVERAGE_LENGTH          
FROM            FISH_INFO