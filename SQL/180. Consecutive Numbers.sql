/*
- 2026-01-10(1)
- 문제 : num에서 세번 연속해서 같은 숫자가 나오는 숫자 구하기
- 접근법:
        1) 윈도우의 LEAD로 하나미룬거, 두개미룬거 만들고
        2) WHERE절에서 num, num_1after, num_2after를 모두 같다고 써줘야하는데, SELECT절에서 연산한 결과물을 바로 where절에서 쓸 수는 없다. 그래서 FROM절 서브쿼리로 감싸준다.
        3) 연속 세번인 수가 뒤에서 또 등장할걸 감안하여 DISTINCT num해준다.
*/

SELECT          DISTINCT num AS ConsecutiveNums
FROM            (
                SELECT          num
                                , LEAD(num, 1) OVER (ORDER BY id) AS num_1after
                                , LEAD(num, 2) OVER (ORDER BY id) AS num_2after
                FROM            logs
                ) nums
WHERE           num = num_1after
                AND num = num_2after

