import pandas as pd
import sys

def validate_csv(path):
    df = pd.read_csv(path)
    required_columns = ["order_id", "customer_id", "product_id", "date", "quantity", "revenue"]

    missing = [col for col in required_columns if col not in df.columns]
    if missing:
        print(f"❌ Missing columns: {missing}")
        sys.exit(1)

    if (df['revenue'] < 0).any():
        print("❌ Negative revenue found!")
        sys.exit(1)

    print(f"✅ {path} passed validation.")

if __name__ == "__main__":
    validate_csv("data/sample/sales_2021_sample.csv")
