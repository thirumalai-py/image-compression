import boto3
import urllib.parse
import time

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Get bucket and key from the event
    bucket = event['Records'][0]['s3']['bucket']['name']
    source_key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
    
    # Safeguard: Skip files already in processed/
    if source_key.startswith("processed/"):
        print(f"Skipping {source_key}: already in 'processed/'")
        return {
            'statusCode': 200,
            'body': f"Skipped: {source_key} is already in 'processed/'"
        }

    filename = source_key.split('/')[-1]  # extract just the file name
    timestamp = int(time.time())  # UNIX timestamp to avoid overwriting
    destination_key = f"processed/{timestamp}_{filename}"

    try:
        # Copy to destination
        s3.copy_object(
            Bucket=bucket,
            CopySource={'Bucket': bucket, 'Key': source_key},
            Key=destination_key
        )
        print(f"Copied {source_key} to {destination_key}")

        # Confirm copy success
        head_response = s3.head_object(Bucket=bucket, Key=destination_key)
        if head_response['ResponseMetadata']['HTTPStatusCode'] == 200:
            print(f"Verified copy. Deleting original: {source_key}")
            s3.delete_object(Bucket=bucket, Key=source_key)
        else:
            print(f"Copy verification failed. Original file not deleted.")

        return {
            'statusCode': 200,
            'body': f"Moved {source_key} to {destination_key}"
        }

    except Exception as e:
        print(f"Error moving file: {str(e)}")
        return {
            'statusCode': 500,
            'body': f"Error: {str(e)}"
        }
