import pandas as pd
import logging

logger = logging.getLogger(__name__)

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean null values and duplicates from the DataFrame"""
    df = df.copy()

    # count null  before cleaning
    null_count = df.isnull().sum().sum()
    logger.info(f"Found{null_count} null values")

    # delete rows at Amount is null
    df = df.dropna(subset=['price'])

    #delete duplicates
    dupes = df.duplicated().sum()
    df = df.drop_duplicates()
    logger.info(f"Removed {dupes} duplicates")

    #Standardize Amount
   # Text columns → lowercase + strip space เสมอ
    df['status'] = df['status'].str.lower().str.strip()
    df['category'] = df['category'].str.lower().str.strip()

    # Date → แปลงเป็น datetime เสมอ
    df['order_date'] = pd.to_datetime(df['order_date'])

    # ตัวเลข → เช็คว่าเป็น numeric จริงมั้ย
    df['price'] = pd.to_numeric(df['price'], errors='coerce')

    # คำนวณยอดรวม
    df['total_amount'] = df['quantity'] * df['price']
    
    return df
def add_features(df: pd.DataFrame) -> pd.DataFrame:
    """Add column"""
    df = df.copy()

    #จาก order_date ดึงเดือนและปีออกมา
    # เพื่อดูว่าเดือนไหนขายดี
    df['month'] = df['order_date'].dt.month
    df['year'] = df['order_date'].dt.year
    df['day_of_week'] = df['order_date'].dt.day_name()

    #แบ่ง total_amount เป็น tier
    # เพื่อดูว่า order ส่วนใหญ่เป็น order เล็กหรือใหญ่
    df['order_tier'] = pd.cut(
        df['total_amount'],
        bins=[0,500,2000, 10000, float('inf')],
        labels=['small', 'medium', 'large', 'very_large']
    )

    # flag order ที่ไม่ได้ completed
    # เพื่อแยกว่า order ไหนนับเป็นยอดขายจริง
    df['is_successful'] = df['status'] == 'completed'

    return df

def transform(df: pd.DataFrame) -> pd.DataFrame:
    """Pipeline หลัก"""
    df = clean_data(df)
    df = add_features(df)
    logger.info(f"Transform complete: {len(df)} rows")
    return df

if __name__ == "__main__":
    df = pd.read_csv("data/raw/ecommerce_orders.csv")
    df = transform(df)
    print(df.shape)
    print(df.head())

    
