SELECT

    product_id,
    product_name,
    category,
    price,
    stock,
    brand

FROM {{ ref('products') }}