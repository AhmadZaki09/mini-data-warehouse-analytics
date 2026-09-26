SELECT

    id AS user_id,
    "firstName" AS first_name,
    "lastName" AS last_name,
    email,
    phone,
    gender,
    age,
    CAST("birthDate" AS DATE) AS birth_date,
    role

FROM {{ source('bronze', 'api_users') }}