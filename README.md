# Mini Data Warehouse Pipeline & Analytics Agent

Pipeline data engineering yang mengintegrasikan **DummyJSON API, Python, Apache Airflow, PostgreSQL, dbt, Docker, dan NAO Analytics Agent** untuk membangun Data Warehouse dan melakukan analisis data menggunakan Natural Language Query.

## Overview

Project ini merupakan implementasi pipeline data dengan pendekatan **Medallion Architecture** yang terdiri dari layer:

- **Bronze** — menyimpan data hasil ekstraksi dari API
- **Silver** — melakukan transformasi dan cleaning menggunakan dbt
- **Gold** — menyediakan data yang telah dimodelkan untuk kebutuhan analitik

Data dari **DummyJSON API** diambil menggunakan Python dan diorkestrasi menggunakan Apache Airflow. Data kemudian dimuat ke PostgreSQL pada layer Bronze dan ditransformasi menggunakan dbt hingga menghasilkan layer Silver dan Gold.

Layer Gold digunakan sebagai sumber data analitik untuk **NAO Analytics Agent**, sehingga pengguna dapat mengajukan pertanyaan menggunakan bahasa natural tanpa harus menulis query SQL secara langsung.

---

### Arsitektur

```text
                    DummyJSON API
                         │
                         ▼
                  Apache Airflow
                         │
                         ▼
                       Bronze
                         │
                         ▼
                        dbt
                         │
                    ┌────┴────┐
                    ▼         ▼
                  Silver     Gold
                              │
                ┌─────────────┼─────────────┐
                │             │             │
                ▼             ▼             ▼
           fact_sales   fact_reviews   dim_product
                                              │
                                           dim_user
                                              │
                                              ▼
                                     NAO Analytics Agent
                                              │
                                              ▼
                                    Natural Language Query
                                              │
                                              ▼
                                      Analysis & Insight

Tujuan Project
Project ini bertujuan untuk:
- Membangun pipeline data dari sumber API hingga Data Warehouse.
- Menerapkan konsep Medallion Architecture.
- Menggunakan Apache Airflow sebagai orkestrator pipeline.
- Menggunakan dbt untuk transformasi dan pengujian data.
- Membangun Data Warehouse pada PostgreSQL.
- Menghasilkan layer Gold yang dapat digunakan sebagai sumber analitik.
- Mengintegrasikan NAO Analytics Agent dengan Data Warehouse.
- Memungkinkan analisis data menggunakan pertanyaan dalam bahasa natural.

Struktur Project :
Mini_Pipeline/
│
├── airflow/
│   └── dags/
│       └── api_pipeline.py
│
├── config/
│   └── ...
│
├── dbt/
│   └── api_project/
│       ├── models/
│       │   ├── staging/
│       │   ├── silver/
│       │   └── gold/
│       │       ├── dim_product.sql
│       │       ├── dim_user.sql
│       │       ├── fact_sales.sql
│       │       └── fact_reviews.sql
│       │
│       └── ...
│
├── elt/
│   └── load_api.py
│
├── nao-agent/
│   └── mini-ecommerce-analytics/
│       └── ...
│
├── .env
├── .gitignore
├── README.md
├── requirements.txt
└── docker-compose.yml

Analytics Agent
Project ini mengintegrasikan NAO Analytics Agent dengan PostgreSQL Data Warehouse.
Konfigurasi Analytics Agent menggunakan:

Data Warehouse
      │
      ▼
 PostgreSQL
 ecommerce_dw
      │
      ▼
     Gold
      │
      ▼
     NAO
      │
      ▼
    Gemini

Current Scope
Project saat ini berfokus pada analisis:
- Penjualan
- Produk
- Kategori
- Pengguna
- Review pelanggan
Data yang digunakan berasal dari DummyJSON sehingga terdapat beberapa keterbatasan, terutama pada data historis transaksi.
fact_sales belum memiliki atribut tanggal transaksi, sehingga analisis tren penjualan berdasarkan periode waktu belum menjadi bagian dari implementasi saat ini.

Future Improvements
Beberapa pengembangan yang dapat dilakukan:
- Menambahkan data historis transaksi.
- Menambahkan atribut tanggal transaksi.
- Meningkatkan validasi SQL yang dihasilkan Analytics Agent.
- Mencegah double counting pada analisis multi-fact.
- Menambahkan data biaya dan keuntungan.
- Menambahkan informasi retur dan status pesanan.
- Mengembangkan analisis bisnis yang lebih komprehensif.

Author
Ahmad Zaki
D3 Teknik Komputer
Universitas Sriwijaya
Kerja Praktik — PT Pupuk Sriwidjaja Palembang
Department of Information Technology
