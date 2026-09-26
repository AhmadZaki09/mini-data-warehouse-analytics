SELECT

    product_id,
    product_name,
    category,
    price,
    stock

FROM {{ ref('products') }}