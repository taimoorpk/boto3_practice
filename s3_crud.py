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

#create file1 and file2
file1 = "file1.txt"
file2 = "file2.txt"

# upload file1 to bucket
s3.Bucket(bucket_name).upload_file(Filename=file1,Key=file1)

# Read the file content

obj = s3.Object(bucket_name,file1)
body = obj.get()["Body"].read()
print(body)

# Update fil1 in the bucket with new content from file2
s3.Object(bucket_name,file1).put(Body=open(file2,'rb'))

body = s3.Object(bucket_name,file1).get()["Body"].read()
print(body)