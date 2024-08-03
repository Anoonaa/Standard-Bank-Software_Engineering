import json
import boto3
import tempfile
from PIL import Image
import numpy as np
from image_encoder import encode_image  # Import the encode_image function

def lambda_handler(event, context):
    s3_client = boto3.client('s3')
    
    # Get the bucket name and image key from the event
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    image_key = event['Records'][0]['s3']['object']['key']
    
    # Download the image file from S3
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        s3_client.download_fileobj(bucket_name, image_key, tmp_file)
        tmp_file.close()
        
        # Encode the image
        encoded_vector = encode_image(tmp_file.name)
    
    # Optionally, you could save the encoded vector to another S3 bucket or process it further here
    
    return {
        'statusCode': 200,
        'body': json.dumps('Image encoded successfully!')
    }

