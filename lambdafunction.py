
import boto3
import json
from datetime import datetime

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = 'desafio-dio-s3' 
    
    file_content = f"Arquivo criado automaticamente em {datetime.now()}"
    file_name = f"lambda_upload_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    
    s3.put_object(
        Bucket=bucket_name,
        Key=file_name,
        Body=file_content
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps(f"Arquivo {file_name} criado no bucket {bucket_name}")
    }

