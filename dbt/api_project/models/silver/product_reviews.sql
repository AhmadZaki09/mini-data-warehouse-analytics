SELECT

    product_id,

    rating,

    comment,

    CAST(review_date AS TIMESTAMP) AS review_date,

    reviewer_name,

    reviewer_email

FROM {{ source('bronze', 'api_product_reviews') }}