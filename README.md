# E-Commerce ETL Pipeline

An end-to-end ETL pipeline for processing e-commerce order data,
built with Python and PostgreSQL.

---

## Project Overview

This project simulates a real-world data engineering workflow for 
an e-commerce platform — extracting raw order data, cleaning and 
transforming it, loading into a structured database, and running 
SQL analysis to identify top-selling products and revenue trends.

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python (Pandas) | Data extraction & transformation |
| PostgreSQL | Data warehouse |
| SQLAlchemy | Database connection |
| SQL (Window Functions) | Data analysis |
| Git / GitHub | Version control |

---

## Pipeline Architecture

```
Raw CSV → Extract → Transform → Load → SQL Analysis
```

- **Extract** — Read raw e-commerce order CSV (1,020 rows)
- **Transform** — Clean nulls, remove duplicates, add derived columns
- **Load** — Store cleaned data into PostgreSQL database
- **Analyze** — SQL queries for sales analysis by product and category

---

## Key Results

- Processed **1,020** order records
- Removed **10** duplicate entries and **20** null values
- Identified top-selling products by quantity and revenue
- Analysed monthly sales trends and category performance

---

## How to Run

**1. Clone the repository**
```bash
git clone https://github.com/mukiskaijeaw/ecommerce-etl-pipeline.git
cd ecommerce-etl-pipeline
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Create sample dataset**
```bash
python create_data.py
```

**4. Set up PostgreSQL**
- Create a database named `ecommerce_db`
- Update DB credentials in `src/load.py` if needed

**5. Run the pipeline**
```bash
python main.py
```

**6. Run SQL analysis**
- Open `sql/analysis_queries.sql` in pgAdmin
- Run queries against `ecommerce_db`

---

## Project Structure

```
ecommerce_etl_pipeline/
├── data/
│   ├── raw/           ← Raw CSV files (not included in repo)
│   └── processed/     ← Processed data
├── src/
│   ├── extract.py     ← Read CSV into DataFrame
│   ├── transform.py   ← Clean and transform data
│   └── load.py        ← Load into PostgreSQL
├── sql/
│   └── analysis_queries.sql  ← SQL analysis queries
├── create_data.py     ← Generate sample dataset
├── main.py            ← Run full ETL pipeline
└── requirements.txt
```

---

## Author

**Chomphunut Unmee**  
Aspiring Data Engineer | Bioscience & Technology Graduate  
[GitHub](https://github.com/mukiskaijeaw)