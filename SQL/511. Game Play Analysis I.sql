/*
- 2026-01-10(2)
- 문제 : 각 플레이어가 처음 로그인한 시점(even_date가 최초로 찍힌 날을 return) 찾기
- 접근법:
        1) ROW_NUMBER() 사용해서 어떤 이벤트가 각 플레이어별로 최초로 발생한 이벤트인지 찾기
            - 각 플레이어별이기 때문에 PARTITION BY player_id
            - 순서도 결정을 해야해서 ORDER BY event_date (옛날꺼부터 순위를 매겨줌)
        2) WHERE rown = 1을 하면 각 플레이어들의 첫번째 활동을 찾을 수 있음(WHERE절에 사용하기 위해FROM의 서브쿼리로 넣어줌)
*/
SELECT          player_id
                , event_date AS first_login
FROM            (
                SELECT          player_id
                                , event_date
                                , ROW_NUMBER() OVER (PARTITION BY player_id ORDER BY event_date) AS rown
                FROM            activity
                ) activity_rown
WHERE           rown = 1

