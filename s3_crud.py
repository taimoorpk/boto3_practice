#import boto3 library
import boto3

# instantiate boto3 resource for S3  and name teh bucket
s3 = boto3.resource("s3")
bucket_name = "bucket-taimoor-crud1"

#check if bucket exist
# create the bucket if it does not exist

all_buckets = [bucket.name for bucket in s3.buckets.all()]
if bucket_name not in all_buckets:
    print(f"'{bucket_name}' does not exist.Creating now....")
    s3.create_bucket(Bucket=bucket_name,
                      CreateBucketConfiguration={'LocationConstraint': 'eu-west-2'})
    print(f"'{bucket_name}' has been created." )
else:
    print(f"'{bucket_name}' bucket already exists.No need to create new one")

for bucket in s3.buckets.all():
    print(bucket.name)

