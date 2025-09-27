-- You must include the WITH clause that defines the temporary tables
WITH cancellation_stats AS (
    -- CTE 1: Calculates cancellation rate for each seller
    SELECT
        oi.seller_id,
        COUNT(o.order_id) AS total_orders,
        (SUM(CASE WHEN o.order_status = 'canceled' THEN 1 ELSE 0 END) * 100.0 / COUNT(o.order_id)) AS cancellation_rate_percent
    FROM
        order_items oi
    JOIN
        orders o ON oi.order_id = o.order_id
    GROUP BY
        oi.seller_id
),
review_stats AS (
    -- CTE 2: Calculates average review score for each seller
    SELECT
        oi.seller_id,
        AVG(rev.review_score) AS avg_review_score
    FROM
        order_items oi
    JOIN
        order_reviews rev ON oi.order_id = rev.order_id
    GROUP BY
        oi.seller_id
)

-- Now, run the main query that USES the CTEs above
-- Query to get the 50 highest-risk sellers
(SELECT cs.seller_id, cs.total_orders, cs.cancellation_rate_percent, rs.avg_review_score,
    (CASE WHEN cs.cancellation_rate_percent > 10 THEN 3 WHEN cs.cancellation_rate_percent > 5 THEN 2 ELSE 0 END +
     CASE WHEN rs.avg_review_score < 2 THEN 3 WHEN rs.avg_review_score < 3.5 THEN 2 ELSE 0 END) AS risk_score
 FROM cancellation_stats cs JOIN review_stats rs ON cs.seller_id = rs.seller_id
 WHERE cs.total_orders > 10
 ORDER BY risk_score DESC, cancellation_rate_percent DESC
 LIMIT 50)

UNION ALL

-- Query to get the 50 lowest-risk sellers
(SELECT cs.seller_id, cs.total_orders, cs.cancellation_rate_percent, rs.avg_review_score,
    (CASE WHEN cs.cancellation_rate_percent > 10 THEN 3 WHEN cs.cancellation_rate_percent > 5 THEN 2 ELSE 0 END +
     CASE WHEN rs.avg_review_score < 2 THEN 3 WHEN rs.avg_review_score < 3.5 THEN 2 ELSE 0 END) AS risk_score
 FROM cancellation_stats cs JOIN review_stats rs ON cs.seller_id = rs.seller_id
 WHERE cs.total_orders > 10
 ORDER BY risk_score ASC, cancellation_rate_percent ASC
 LIMIT 50);