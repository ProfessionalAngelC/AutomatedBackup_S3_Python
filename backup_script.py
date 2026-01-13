"""
backup_script.py

Automates daily backup of sensitive local files to AWS S3 with versioning enabled.
"""

import boto3
import os
from datetime import datetime

# === CONFIGURATION ===
BUCKET_NAME = 'angel-backup-bucket'  # Replace with your S3 bucket name
LOCAL_FOLDER = r'C:\SensitiveFiles'   # Replace with your local folder path

# Initialize S3 client
s3 = boto3.client('s3')

def upload_files():
    """
    Upload all files from LOCAL_FOLDER to S3 bucket with timestamped keys.
    """
    for root, dirs, files in os.walk(LOCAL_FOLDER):
        for file in files:
            local_path = os.path.join(root, file)
            s3_key = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_{file}"
            try:
                s3.upload_file(local_path, BUCKET_NAME, s3_key)
                print(f"Uploaded {local_path} to s3://{BUCKET_NAME}/{s3_key}")
            except Exception as e:
                print(f"Failed to upload {local_path}: {e}")

if __name__ == "__main__":
    upload_files()
