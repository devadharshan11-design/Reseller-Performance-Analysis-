SELECT
    s.seller_state AS state,
    SUM(oi.price) AS total_revenue,
    COUNT(DISTINCT s.seller_id) AS number_of_resellers
FROM
    sellers s
JOIN
    order_items oi ON s.seller_id = oi.seller_id
GROUP BY
    s.seller_state
ORDER BY
    total_revenue DESC
LIMIT 10;