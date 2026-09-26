SELECT

    ci.cart_id,

    c.user_id,

    ci.product_id,

    ci.quantity,

    ROUND(ci.price::numeric, 2) AS price,

    ROUND(ci.total::numeric, 2) AS total,

    ROUND(ci.discount_percentage::numeric, 2) AS discount_percentage,

    ROUND(ci.discounted_total::numeric, 2) AS discounted_total,

    ROUND((ci.total - ci.discounted_total)::numeric, 2) AS discount_amount

FROM {{ ref('cart_items') }} ci

JOIN {{ ref('carts') }} c
ON ci.cart_id = c.cart_id