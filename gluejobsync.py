import boto3

file_path = 'tbff20001_metrica/'
s3 = boto3.resource('s3')
source_bucket = s3.Bucket('metricsdev-src-bucket')
destination_bucket = s3.Bucket('metricsdev-dst-bucket')
destination_keys = [object.key for object in destination_bucket.objects.all()]
for object in source_bucket.objects.all():
  if (object.key not in destination_keys):
    copy_source = {
        'Bucket': 'metricsdev-src-bucket',
        'Key': object.key
    }
    destination_bucket.copy(copy_source, file_path+object.key)