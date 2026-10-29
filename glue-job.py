import boto3
import csv
from pathlib import Path

# Read sample e-commerce data from a local CSV file
input_file = Path("data/orders.csv")

if not input_file.exists():
    print("Orders file not found:", input_file)
else:
    with input_file.open(
        mode="r", newline="", encoding="utf-8"
    ) as file:
        reader = csv.DictReader(file)

        for order in reader:
            print(order)

# AWS S3 client uses your configured AWS credentials
s3 = boto3.client("s3")

# Example: upload a processed file to your own S3 bucket
# Replace the placeholders before running.
# s3.upload_file(
#     "data/processed_orders.csv",
#     "YOUR_S3_BUCKET_NAME",
#     "processed/processed_orders.csv
