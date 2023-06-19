import boto3
import json

def lambda_handler(event, context):
    # Create an S3 client
    s3 = boto3.client('s3')

    # Define the bucket and object key
    bucket_name = 'demodb12'
    object_key = 'data_entry'

    # Define your JSON data
    json_data = [
                {
                "id": "5ac6be6b-8064-4159-9de6-89178a9f8a54",
                "firstname": "Matt",
                "lastname": "Hansen"
                },
                {
                "id": "4b912da3-66aa-45c1-a87f-9f79a256e570",
                "firstname": "Brad",
                "lastname": "Lunsford"
                }]

    # Convert the JSON data to string
    json_string = json.dumps(json_data)

    # Upload the data to S3
    s3.put_object(Body=json_string, Bucket=bucket_name, Key=object_key)

    return {
        'statusCode': 200,
        'body': 'JSON data uploaded to S3 successfully'
    }
