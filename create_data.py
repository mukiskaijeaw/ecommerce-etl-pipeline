import pandas as pd
import random
from datetime import datetime, timedelta

random.seed(42)

products = [
    {"product_id": "P001", "product_name": "iPhone Case", "category": "Electronics", "price": 299},
    {"product_id": "P002", "product_name": "Running Shoes", "category": "Fashion", "price": 1590},
    {"product_id": "P003", "product_name": "Water Bottle", "category": "Sports", "price": 450},
    {"product_id": "P004", "product_name": "Notebook", "category": "Stationery", "price": 89},
    {"product_id": "P005", "product_name": "Wireless Earbuds", "category": "Electronics", "price": 2490},
    {"product_id": "P006", "product_name": "Yoga Mat", "category": "Sports", "price": 890},
    {"product_id": "P007", "product_name": "Face Cream", "category": "Beauty", "price": 599},
    {"product_id": "P008", "product_name": "Coffee Mug", "category": "Kitchen", "price": 199},
]

rows = []
start_date = datetime(2024, 1, 1)

for i in range(1000):
    product = random.choice(products)
    order_date = start_date + timedelta(days=random.randint(0, 364))
    quantity = random.randint(1, 5)
    
    rows.append({
        "order_id": f"ORD{i+1:04d}",
        "product_id": product["product_id"],
        "product_name": product["product_name"],
        "category": product["category"],
        "customer_id": f"CUST{random.randint(1, 200):03d}",
        "quantity": quantity,
        "price": product["price"],
        "order_date": order_date.strftime("%Y-%m-%d"),
        "status": random.choice(["completed", "completed", "completed", "cancelled", "returned"]),
    })

# ใส่ duplicate และ null จงใจ เพื่อฝึก clean
rows += rows[:20]  # duplicate 20 rows
for i in range(10):
    rows[i]["price"] = None  # null 10 rows

df = pd.DataFrame(rows)
df.to_csv("data/raw/ecommerce_orders.csv", index=False)
print(f"Created dataset: {len(df)} rows")