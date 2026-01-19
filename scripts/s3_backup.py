import os
import boto3
from datetime import datetime



SOURCE_DIRECTORY = r"C:\Users\AngelNoeCastañedaPad\OneDrive - WA Evergreen Insulation\Cloud projects\Automated back up project\CompanyData\SensitiveFiles"
S3_BUCKET_NAME = "company-secure-backups-angelcastaneda" 
AWS_REGION = "us-east-1"  



s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=AWS_REGION
)



def backup_files():
    backup_date = datetime.now().strftime("%Y-%m-%d")

    for root, _, files in os.walk(SOURCE_DIRECTORY):
        for file in files:
            local_file_path = os.path.join(root, file)

            relative_path = os.path.relpath(local_file_path, SOURCE_DIRECTORY)
            s3_object_key = f"{backup_date}/{relative_path}"

            try:
                s3.upload_file(local_file_path, S3_BUCKET_NAME, s3_object_key)
                print(f"Uploaded: {s3_object_key}")
            except Exception as error:
                print(f"ERROR uploading {local_file_path}: {error}")

if __name__ == "__main__":
    backup_files()

