"""
Example to download nightlight data from an S3 bucket
References:
https://blogs.worldbank.org/opendata/light-every-night-new-nighttime-light-data-set-and-tools-development
https://registry.opendata.aws/wb-light-every-night/

light-every-night-file-structure:
https://worldbank.github.io/OpenNightLights/wb-light-every-night-readme.html 

bucket:
s3://globalnightlight//F162017/ --no-sign-request

install boto:
!pip install boto3
"""

import boto3
import os
import pandas as pd
from botocore import UNSIGNED
from botocore.config import Config

# get the bucket
s3_resource = boto3.resource('s3', config=Config(signature_version=UNSIGNED))
bucket = s3_resource.Bucket(name='globalnightlight')

# see what file are in the bucket 
for obj in bucket.objects.all(): print(os.path.join(obj.bucket_name, obj.key))
 
# do what you want with the files
for file in bucket.objects.all():
    # for example:
    if 'filter' in file.key:
        print(file.key)
        # new_df = pd.read_csv('s3:://{bucket_name}/{}'.format(file.key))
