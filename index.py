import json
import base64
import urllib
import boto3
import os

bucket_name = os.environ.get('BUCKET_NAME')

session = boto3.session.Session()
s3 = session.client(
    service_name='s3',
    endpoint_url='https://storage.yandexcloud.net'
)

def handler(event, context):
    
    if event['isBase64Encoded'] == True:
        payload = json.loads( base64.b64decode(event['body'].encode('ascii')).decode('utf-8'))
    else:
        payload = json.loads(event['body'])
    
    worker = payload['environmentVariables']['appveyor_build_worker_image']
    if 'deploy_platform_id' in payload['environmentVariables']:
        platform_id = payload['environmentVariables']['deploy_platform_id']
    else:
        platform_id = worker
    
    base = payload['projectSlug'] + '/' + payload['branch'] + '/' + platform_id

    for artifact in payload['artifacts']:
        key = base + '/' + artifact['name']
        response = urllib.request.urlopen(artifact['url'])
        data = response.read()
        s3.put_object(Bucket=bucket_name, Key=key, Body=data)
    
    return {
        'statusCode': 200,
        'body': base,
    }
