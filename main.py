import logging
import sys
sys.path.append('src')

from extract import extract_data
from transform import transform
from load import load_data
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'

)

def run_pipeline(filepath: str):
    print("=" * 50)
    print("E-commerce DAta Pipeline")
    print("=" * 50)

    # Step1: Extract
    raw_df = extract_data(filepath)

    # Step2: Transform
    clean_df = transform(raw_df)

    #Step3: Load
    load_data(clean_df, mode='replace')

    print("=" * 50)
    print(f"✓ PIPELINE COMPLETE!")
    print(f"✓ Total records loaded: {len(clean_df)}")
    print("=" * 50)

if __name__ == "__main__":
    run_pipeline('data/raw/ecommerce_orders.csv')

