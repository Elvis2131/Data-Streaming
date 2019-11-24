import boto3
import csv
import json
import time

regionName = 'us-east-1'

aws_conn = boto3.client('kinesis', region_name=regionName)

streamName = 'blossom-data-eng-Elvis'

aws_conn.list_streams()

response = aws_conn.create_stream(StreamName=streamName, ShardCount=1)
aws_conn.list_streams()
stream_description = aws_conn.describe_stream(StreamName=streamName)
stream_description.keys()


