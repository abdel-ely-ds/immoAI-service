import json
import urllib.request


def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))

    API_ENDPOINT = "http://<ec2-instance-public-ip>:<port>/reload"

    req = urllib.request.Request(API_ENDPOINT, method="POST")

    try:
        response = urllib.request.urlopen(req)
        print("Reload API called successfully")
    except Exception as e:
        print(f"Failed to call reload API: {e}")

    return {
        "statusCode": 200,
        "body": json.dumps("Lambda for reloading data was executed!"),
    }
