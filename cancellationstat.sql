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
-- Final SELECT: Joins the CTEs and calculates the risk score
SELECT
    cs.seller_id,
    cs.total_orders,
    cs.cancellation_rate_percent,
    rs.avg_review_score,
    -- This is our scoring logic
    (
        CASE
            WHEN cs.cancellation_rate_percent > 10 THEN 3 -- High cancellation rate = 3 points
            WHEN cs.cancellation_rate_percent > 5  THEN 2 -- Medium cancellation rate = 2 points
            ELSE 0
        END
        +
        CASE
            WHEN rs.avg_review_score < 2 THEN 3 -- Very bad reviews = 3 points
            WHEN rs.avg_review_score < 3.5 THEN 2 -- Mediocre reviews = 2 points
            ELSE 0
        END
    ) AS risk_score
FROM
    cancellation_stats cs
JOIN
    review_stats rs ON cs.seller_id = rs.seller_id
WHERE
    cs.total_orders > 10 -- We only score sellers with at least 10 orders
ORDER BY
    risk_score DESC, cancellation_rate_percent DESC
LIMIT 20;