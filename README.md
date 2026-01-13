# Week 2: Automated Backup for Sensitive Documents

## Project Goal
Automate daily backup of sensitive files (e.g., invoices, PSE records) to AWS S3 with versioning enabled using Python.  

## Setup Instructions
1. Configure AWS CLI with your access keys:  
   ```bash
   aws configure
Install Python dependencies:

bash
Copy code
pip install boto3
Modify backup_script.py:

Set BUCKET_NAME to your S3 bucket.

Set LOCAL_FOLDER to the folder containing files to back up.

Run script to test manual backup:

bash
Copy code
python backup_script.py
(Optional) Schedule daily automatic backups via Windows Task Scheduler
