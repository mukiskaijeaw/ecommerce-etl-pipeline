import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def extract_data(file_path: str) -> pd.DataFrame:
    """reads CSV file"""
    logger.info(f"Extracting data from {file_path}")

    df = pd.read_csv(file_path)

    logger.info(f"Extracted {len(df)} rows, {len(df.columns)} columns")
    return df

if __name__ == "__main__":
    df = extract_data("data/raw/ecommerce_orders.csv")
    print(df.shape)
    print(df.head())