# python 3

import os
source_bucket = "metricsdev-src-bucket"
target_bucket = "metricsdev-dst-bucket"
target_path = "tbff20001_metrica"
sync_command = f"aws s3 sync s3://$source_bucket/ s3://$target_bucket/$target_path/"
os.system(sync_command)