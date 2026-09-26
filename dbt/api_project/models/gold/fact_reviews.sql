SELECT

    r.product_id,

    u.user_id,

    r.rating,

    r.comment,

    r.review_date,

    r.reviewer_name,

    r.reviewer_email

FROM {{ ref('product_reviews') }} r

LEFT JOIN {{ ref('dim_user') }} u
    ON LOWER(r.reviewer_email) = LOWER(u.email)