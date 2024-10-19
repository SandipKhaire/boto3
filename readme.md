## Locally Accessing AWS services using python Boto3 SDK 

In this porject we will see,how can we use Boto3 SDK to connect aws account and use the services like creating s3 bucket and listing s3 buckets from python command line.

## Step 1: Install Boto3
  > pip install boto3

## Step 2: Set Up AWS Credentials
Before using Boto3, make sure you have set up your AWS credentials either via the aws configure command or environment variables. Boto3 will automatically use these credentials to interact with AWS services.I have directly used Credentitals in the script but this is not recommended for prouduction level.Because this will be security concern.


## Step 3: Python Script to Create an S3 Bucket
Refer S3_launch.py script.

**Note** :
- **Bucket Naming Rules:** Make sure that your bucket name follows AWS bucket naming rules:
    * Must be unique globally.
    * Must be between 3 and 63 characters long.
    * Must not contain uppercase characters or underscores.
    * Must start and end with a lowercase letter or number.
