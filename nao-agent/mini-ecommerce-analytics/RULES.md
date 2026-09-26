# Gold Database Reference

## Database

Database name:
ecommerce_dw

Schema:
gold

## Gold Models

The following dbt models are materialized in PostgreSQL database `ecommerce_dw`, schema `gold`:

- dim_product
- dim_user
- fact_sales
- fact_reviews

## dim_product

Columns:
- product_id
- product_name
- category
- price
- stock

Primary key:
product_id

## dim_user

Columns:
- user_id
- first_name
- last_name
- email
- phone
- gender
- age
- birth_date
- role

Primary key:
user_id

## fact_sales

Columns:
- cart_id
- user_id
- product_id
- quantity
- price
- total
- discount_percentage
- discounted_total
- discount_amount

Relationships:
- product_id -> dim_product.product_id
- user_id -> dim_user.user_id

## fact_reviews

Columns:
- product_id
- rating
- comment
- review_date
- reviewer_name
- reviewer_email

Relationship:
- product_id -> dim_product.product_id

## Important

Always use:

Database: ecommerce_dw
Schema: gold

Never use public schema for Gold models.

The product name column is:
dim_product.product_name

The sales amount column is:
fact_sales.total

The discounted sales amount column is:
fact_sales.discounted_total