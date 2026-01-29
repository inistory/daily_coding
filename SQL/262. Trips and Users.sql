/*
- 2026-01-29(1)
- 문제: client와 driver가 banned가 아닌 것 출력
- 접근법:
    1) 전체 트립테이블에서 banned된 유저로부터 발생한 로그를 JOIN을 통해 지우기
     - client도 banned된 사람이 아니고, driver도 banned된 사람이 아닌 trip만 결과가 남게하기
    2) 이 결과를 일별로 결과 요약: GROUP BY request_at
    3) 'cancelled_by_driver', 'cancelled_by_client' 둘다 cancel에 포함되는 것이므로 해당 status일 때의 경우의 id를 COUNT
    4) ROUND로 소숫점 둘째짜리까지 출력

*/
WITH trips_daily AS (
            SELECT          request_at
                            , COUNT(CASE WHEN status IN ('cancelled_by_driver', 'cancelled_by_client') THEN id END) AS cancelled_trip
                            , COUNT(id) AS total_trip
            FROM            trips AS t
            INNER JOIN      users AS c -- client
            ON              t.client_id = c.users_id
            AND             c.banned = 'No'
            INNER JOIN      users AS d -- driver
            ON              t.driver_id = d.users_id
            AND             d.banned = 'No'
            WHERE           request_at BETWEEN '2013-10-01' AND '2013-10-03'
            GROUP BY        request_at
)

SELECT          request_at AS DAY
                , ROUND(cancelled_trip / total_trip, 2) AS 'Cancellation Rate'
FROM            trips_daily
