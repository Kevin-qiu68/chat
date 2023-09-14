import json

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!'),
        'headers':{
            'Access-Control-Allow-Origin':'*'
        }
    }
