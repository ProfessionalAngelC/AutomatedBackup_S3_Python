# Automated S3 Backup for Sensitive Business Documents

## Project Overview
This project demonstrates the design and implementation of an automated cloud backup solution using AWS S3 and Python. The solution securely backs up sensitive business documents from a Windows environment to Amazon S3 with versioning enabled, supporting basic disaster recovery and data protection requirements.

The project is designed to reflect a real-world small business use case and is documented as a portfolio-ready cloud project.

---

## Business Problem
Small businesses often store critical operational documents (such as invoices, payroll data, or compliance records) locally on employee machines or shared drives. This creates several risks:

- Data loss due to hardware failure
- Accidental deletion or overwrites
- Ransomware or malware incidents
- Lack of offsite backups

Without an automated and versioned backup system, recovering lost data can be costly or impossible.

---

## Solution
This project implements an automated backup workflow that:

- Uses a Python script to scan a local directory for sensitive files
- Uploads files to an Amazon S3 bucket
- Organizes backups by date
- Enables S3 versioning to protect against accidental overwrites or deletions
- Uses IAM credentials with least-privilege access

The solution is simple, cost-effective, and suitable for small business environments.

---

## Architecture Overview

**Backup Workflow:**

Local Windows Files  
→ Python Backup Script (boto3)  
→ AWS S3 Bucket (Versioning Enabled)

A visual diagram of this workflow is included in the `diagrams/` folder.

---

## Technologies Used

- **AWS S3** – Cloud object storage
- **AWS IAM** – Secure access control
- **Python 3** – Automation scripting
- **boto3** – AWS SDK for Python
- **Windows 11** – Local execution environment
- **Git & GitHub** – Version control and documentation

---

## Security Considerations

- IAM user is scoped to S3 access only (least privilege)
- AWS credentials are stored as environment variables (not hard-coded)
- Sensitive files are excluded from the repository using `.gitignore`
- S3 versioning protects against accidental data loss

---

## How the Backup Script Works

1. Defines a local source directory containing sensitive files
2. Walks through all files in the directory
3. Uploads each file to S3 under a date-based prefix
4. Prints upload status for verification
5. Relies on environment variables for AWS credentials

---

## Screenshots

Screenshots documenting the setup and successful execution are located in:

