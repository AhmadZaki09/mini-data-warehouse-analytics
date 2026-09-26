import pandas as pd
import requests

from airflow.providers.postgres.hooks.postgres import PostgresHook


def load_api_to_bronze():

    # ======================================================
    # PostgreSQL Connection
    # ======================================================

    engine = PostgresHook(
        postgres_conn_id="test"
    ).get_sqlalchemy_engine()

    # ======================================================
    # API Endpoint
    # ======================================================

    USERS_API = "https://dummyjson.com/users?limit=0"
    PRODUCTS_API = "https://dummyjson.com/products?limit=0"
    CARTS_API = "https://dummyjson.com/carts?limit=0"

    print("=" * 60)
    print("Loading API Data to Bronze Layer...")
    print("=" * 60)

    # ======================================================
    # USERS
    # ======================================================

    print("\nLoading Users...")

    users = requests.get(USERS_API).json()["users"]

    df_users = pd.DataFrame(users)

    # Ambil kolom yang dibutuhkan saja
    df_users = df_users[
        [
            "id",
            "firstName",
            "lastName",
            "email",
            "phone",
            "gender",
            "age",
            "birthDate",
            "role",
        ]
    ]

    df_users.to_sql(
        "api_users",
        engine,
        schema="bronze",
        if_exists="replace",
        index=False,
    )

    print(f"Users : {len(df_users)}")

    # ======================================================
    # PRODUCTS
    # ======================================================

    print("\nLoading Products...")

    products = requests.get(PRODUCTS_API).json()["products"]

    df_products = pd.DataFrame(products)

    # Pilih kolom penting saja
    columns = [
        "id",
        "title",
        "category",
        "price",
        "stock",
    ]

    # Kalau brand tersedia, ikut disimpan
    if "brand" in df_products.columns:
        columns.append("brand")

    df_products = df_products[columns]

    df_products.to_sql(
        "api_products",
        engine,
        schema="bronze",
        if_exists="replace",
        index=False,
    )

    print(f"Products : {len(df_products)}")

    # ======================================================
    # PRODUCT REVIEWS
    # ======================================================

    print("\nLoading Product Reviews...")

    review_rows = []

    for product in products:

        for review in product.get("reviews", []):

            review_rows.append(
                {
                    "product_id": product["id"],
                    "rating": review["rating"],
                    "comment": review["comment"],
                    "review_date": review["date"],
                    "reviewer_name": review["reviewerName"],
                    "reviewer_email": review["reviewerEmail"],
                }
            )

    df_reviews = pd.DataFrame(review_rows)

    df_reviews.to_sql(
        "api_product_reviews",
        engine,
        schema="bronze",
        if_exists="replace",
        index=False,
    )

    print(f"Product Reviews : {len(df_reviews)}")

    # ======================================================
    # CARTS
    # ======================================================

    print("\nLoading Carts...")

    carts = requests.get(CARTS_API).json()["carts"]

    cart_rows = []
    cart_item_rows = []

    for cart in carts:

        # --------------------------------------------------
        # CART HEADER
        # --------------------------------------------------

        cart_rows.append(
            {
                "cart_id": cart["id"],
                "user_id": cart["userId"],
                "total": cart["total"],
                "discounted_total": cart["discountedTotal"],
                "total_products": cart["totalProducts"],
                "total_quantity": cart["totalQuantity"],
            }
        )

        # --------------------------------------------------
        # CART ITEMS
        # --------------------------------------------------

        for product in cart["products"]:

            cart_item_rows.append(
                {
                    "cart_id": cart["id"],
                    "product_id": product["id"],
                    "quantity": product["quantity"],
                    "price": product["price"],
                    "total": product["total"],
                    "discount_percentage": product["discountPercentage"],
                    "discounted_total": product["discountedTotal"],
                }
            )

    df_carts = pd.DataFrame(cart_rows)
    df_cart_items = pd.DataFrame(cart_item_rows)

    # ======================================================
    # LOAD CARTS TO BRONZE
    # ======================================================

    df_carts.to_sql(
        "api_carts",
        engine,
        schema="bronze",
        if_exists="replace",
        index=False,
    )

    df_cart_items.to_sql(
        "api_cart_items",
        engine,
        schema="bronze",
        if_exists="replace",
        index=False,
    )

    print(f"Carts : {len(df_carts)}")
    print(f"Cart Items : {len(df_cart_items)}")

    # ======================================================
    # FINISH
    # ======================================================

    print("\n" + "=" * 60)
    print("Semua API berhasil dimasukkan ke Bronze!")
    print("=" * 60)

    print("\nBronze Tables:")
    print("- api_users")
    print("- api_products")
    print("- api_product_reviews")
    print("- api_carts")
    print("- api_cart_items")