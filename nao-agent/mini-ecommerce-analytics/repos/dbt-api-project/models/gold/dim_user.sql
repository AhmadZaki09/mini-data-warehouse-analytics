SELECT

    user_id,
    first_name,
    last_name,
    email,
    phone,
    gender,
    age,
    birth_date,
    role

FROM {{ ref('users') }}