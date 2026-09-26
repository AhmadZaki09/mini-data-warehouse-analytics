SELECT

    id AS product_id,
    title AS product_name,
    category,
    price,
    stock

FROM {{ source('bronze', 'api_products') }}