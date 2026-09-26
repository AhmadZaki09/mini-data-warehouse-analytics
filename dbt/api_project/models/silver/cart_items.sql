SELECT

    cart_id,
    product_id,
    quantity,
    price,
    total,
    discount_percentage,
    discounted_total

FROM {{ source('bronze', 'api_cart_items') }}