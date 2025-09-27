SELECT
    s.seller_id,
    COUNT(o.order_id) AS total_orders,
    SUM(CASE WHEN o.order_status = 'canceled' THEN 1 ELSE 0 END) AS canceled_orders,
    -- We multiply by 100.0 to get a percentage with decimals
    (SUM(CASE WHEN o.order_status = 'canceled' THEN 1 ELSE 0 END) * 100.0 / COUNT(o.order_id)) AS cancellation_rate_percent
FROM
    sellers s
JOIN
    order_items oi ON s.seller_id = oi.seller_id
JOIN
    orders o ON oi.order_id = o.order_id
GROUP BY
    s.seller_id
HAVING
    COUNT(o.order_id) > 20 -- To ensure we only look at sellers with a meaningful number of orders
ORDER BY
    cancellation_rate_percent DESC
LIMIT 15;