/*
- 문제 : ~
- 접근법: ~
*/

SELECT          t1.a
                , t2.b
FROM
                (
                /* 유저의 가입정보를 불러옴 */
                SELECT          c_id
                                , user_id
                                , bas_date,
                                , fff
                FROM            db.table
                WHERE           1=1
                AND             base_date >= '2025-01-01'
                AND             c_id not in ('a', 'b')
                ) t1
/* +BROADCAST */ LEFT JOIN
                (
                /* 유저의 신용정보를 불러옴 */
                adfjkd;fj
                dasfl;kjaf;l    
                ) t2
ON              t1.a = t2.b


;


/*데이터 조회 방법*/
SELECT *
FROM DB.table
limit 10

;


