import boto3
from botocore.exceptions import ClientError

session = boto3.Session(
    # pass your credentials
)

# Now you can use session to create your client/resource
s3 = session.client('s3')

def create_s3_bucket(bucket_name, region=None):
    try:
        if region is None:
            s3.create_bucket(Bucket=bucket_name)
        else:
            s3.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={'LocationConstraint': region}
            )
        print(f"Bucket {bucket_name} created successfully.")
    except ClientError as e:
        print(f"Error: {e}")
        return False
    return True

# Example usage
bucket_name = "newbuckettocreate"  # Make sure this is unique across all AWS accounts
region = None # Specify your region

if __name__=="__main__":
    create_s3_bucket(bucket_name, region)
    # List all S3 buckets
    response = s3.list_buckets()
    for bucket in response['Buckets']:
        print(bucket['Name'])